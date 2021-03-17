from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')

class DashboardBoutiqueSearchForm(forms.Form):
    name = forms.CharField(label=_('Boutique name'), required=False)
    city = forms.CharField(label=_('City'), required=False)

    def is_empty(self):
        d = getattr(self, 'cleaned_data', {})
        def empty(key): return not d.get(key, None)
        return empty('name') and empty('city')

    def apply_city_filter(self, qs, value):
        words = value.replace(',', ' ').split()
        q = [Q(city__icontains=word) for word in words]
        return qs.filter(*q)

    def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)

    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs


class DashboardBoutiqueCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Boutique
        fields = ('name', 'manager', 'city')

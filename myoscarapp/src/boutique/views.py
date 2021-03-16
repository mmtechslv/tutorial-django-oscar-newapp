from django.views import generic
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')


class BoutiqueListView(generic.ListView):
    model = Boutique
    template_name = 'boutique/boutique_list.html'
    context_object_name = 'boutique_list'


class BoutiqueDetailView(generic.DetailView):
    model = Boutique
    template_name = 'boutique/boutique_details.html'
    context_object_name = 'boutique'

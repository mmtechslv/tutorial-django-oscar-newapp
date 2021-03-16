from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


class BoutiqueConfig(OscarConfig):
    name = 'boutique'
    namespace = 'boutique'

    def ready(self):
        super().ready()
        self.boutique_list_view = get_class(
            'boutique.views', 'BoutiqueListView')
        self.boutique_detail_view = get_class(
            'boutique.views', 'BoutiqueDetailView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.boutique_list_view.as_view(), name='index'),
            re_path(r'^view/(?P<pk>\d+)/$',
                    self.boutique_detail_view.as_view(), name='details'),
        ]
        return self.post_process_urls(urls)

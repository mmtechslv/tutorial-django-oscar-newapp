from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class


class DashboardConfig(OscarDashboardConfig):
    name = 'boutique.dashboard'
    label = 'boutique_dashboard'
    namespace = 'boutique-dashboard'

    default_permissions = ['is_staff']

    def ready(self):
        self.boutique_list_view = get_class(
            'boutique.dashboard.views', 'DashboardBoutiqueListView')
        self.boutique_create_view = get_class(
            'boutique.dashboard.views', 'DashboardBoutiqueCreateView')
        self.boutique_update_view = get_class(
            'boutique.dashboard.views', 'DashboardBoutiqueUpdateView')
        self.boutique_delete_view = get_class(
            'boutique.dashboard.views', 'DashboardBoutiqueDeleteView')

    def get_urls(self):
        urls = [
            path('', self.boutique_list_view.as_view(), name='boutique-list'),
            path('create/', self.boutique_create_view.as_view(),
                 name='boutique-create'),
            path('update/<int:pk>/', self.boutique_update_view.as_view(),
                 name='boutique-update'),
            path('delete/<int:pk>/', self.boutique_delete_view.as_view(),
                 name='boutique-delete'),
        ]
        return self.post_process_urls(urls)

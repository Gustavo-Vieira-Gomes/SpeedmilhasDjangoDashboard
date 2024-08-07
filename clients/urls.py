from django.urls import path
from clients.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView


urlpatterns = [
    path('clients/list/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/detail/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]

from django.urls import path
from .views import CanceledLapsListView, CanceledLapsCreateView, CanceledLapsDetailView, CanceledLapsUpdateView, CanceledLapsDeleteView


urlpatterns = [
    path('canceledlap/list/', CanceledLapsListView.as_view(), name='canceledlap_list'),
    path('canceledlap/create/', CanceledLapsCreateView.as_view(), name='canceledlap_create'),
    path('canceledlap/<int:pk>/detail/', CanceledLapsDetailView.as_view(), name='canceledlap_detail'),
    path('canceledlap/<int:pk>/update/', CanceledLapsUpdateView.as_view(), name='canceledlap_update'),
    path('canceledlap/<int:pk>/delete/', CanceledLapsDeleteView.as_view(), name='canceledlap_delete'),
]
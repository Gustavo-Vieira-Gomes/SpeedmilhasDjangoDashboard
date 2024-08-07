from django.urls import path
from airlines.views import AirlineListView, AirlineCreateView, AirlineUpdateView, AirlineDetailView, AirlineDeleteView


urlpatterns = [
    path('airlines/list/', AirlineListView.as_view(), name='airline_list'),
    path('airlines/create/', AirlineCreateView.as_view(), name='airline_create'),
    path('airlines/<int:pk>/detail/', AirlineDetailView.as_view(), name='airline_detail'),
    path('airlines/<int:pk>/update/', AirlineUpdateView.as_view(), name='airline_update'),
    path('airlines/<int:pk>/delete/', AirlineDeleteView.as_view(), name='airline_delete'),
]

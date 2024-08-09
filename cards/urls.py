from django.urls import path
from cards.views import CardListView, CardCreateView, CardUpdateView, CardDetailView, CardDeleteView


urlpatterns = [
    path('cards/list/', CardListView.as_view(), name='card_list'),
    path('cards/create/', CardCreateView.as_view(), name='card_create'),
    path('cards/<int:pk>/detail/', CardDetailView.as_view(), name='card_detail'),
    path('cards/<int:pk>/update/', CardUpdateView.as_view(), name='card_update'),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
]
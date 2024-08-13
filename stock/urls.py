from django.urls import path
from .views import StockListView, StockCreateView, StockUpdateView, StockDetailView, StockDeleteView


urlpatterns = [
    path('stock/list/', StockListView.as_view(), name='stock_list'),
    path('stock/create/', StockCreateView.as_view(), name='stock_create'),
    path('stock/<int:pk>/detail/', StockDetailView.as_view(), name='stock_detail'),
    path('stock/<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('stock/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
]
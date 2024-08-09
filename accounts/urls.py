from django.urls import path
from accounts.views import AccountListView, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView


urlpatterns = [
    path('accounts/list/', AccountListView.as_view(), name='account_list'),
    path('accounts/create/', AccountCreateView.as_view(), name='account_create'),
    path('accounts/<int:pk>/detail', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/<int:pk>/update', AccountUpdateView.as_view(), name='account_update'),
    path('accounts/<int:pk>/delete', AccountDeleteView.as_view(), name='account_delete'),
]

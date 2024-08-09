from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from accounts.models import Account
from django.urls import reverse_lazy
from accounts.forms import AccountForm


class AccountListView(ListView):
    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        holder = self.request.GET.get('holder')
        account_login = self.request.GET.get('account_login')
        holder_id = self.request.GET.get('holder_id')
        account_number = self.request.GET.get('account_number')

        if holder:
            queryset = queryset.filter(holder__icontains=holder)
        if account_login:
            queryset = queryset.filter(account_login__icontains=account_login)
        if holder_id:
            queryset = queryset.filter(holder_id__icontains=holder_id)
        if account_number:
            queryset = queryset.filter(account_number__icontains=account_number)

        return queryset
    

class AccountCreateView(CreateView):
    model = Account
    template_name = 'account_create.html'
    success_url = reverse_lazy('account_list')
    form_class = AccountForm


class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'account_update.html'
    success_url = reverse_lazy('account_list')
    form_class = AccountForm


class AccountDetailView(DetailView):
    model = Account
    template_name = 'account_detail.html'


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account_delete.html'
    success_url = reverse_lazy('account_list')

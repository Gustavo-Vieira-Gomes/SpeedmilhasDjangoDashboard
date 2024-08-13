from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Stock
from django.urls import reverse_lazy
from .forms import StockForm


class StockListView(ListView):
    model = Stock
    template_name = 'stock_list.html'
    context_object_name = 'stock'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        holder = self.request.GET.get('holder')
        account_login = self.request.GET.get('account_login')
        owner  = self.request.GET.get('owner')

        if holder:
            queryset = queryset.filter(account__holder__icontains=holder)

        if account_login:
            queryset = queryset.filter(account__account_login__icontains=account_login)

        if owner:
            queryset = queryset.filter(owner__icontains=owner)

        return queryset
    

class StockCreateView(CreateView):
    model = Stock
    template_name = 'stock_create.html'
    success_url = reverse_lazy('stock_list')
    form_class = StockForm


class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock_detail.html'


class StockUpdateView(UpdateView):
    model = Stock
    template_name = 'stock_update.html'
    success_url = reverse_lazy('stock_list')
    form_class = StockForm


class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stock_delete.html'
    success_url = reverse_lazy('stock_list')

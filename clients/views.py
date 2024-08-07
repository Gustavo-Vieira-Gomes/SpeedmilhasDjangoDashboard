from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from clients.models import Client
from django.urls import reverse_lazy
from clients.forms import ClientForm


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_create.html'
    success_url = reverse_lazy('client_list')
    form_class = ClientForm


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    success_url = reverse_lazy('client_list')
    form_class = ClientForm


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

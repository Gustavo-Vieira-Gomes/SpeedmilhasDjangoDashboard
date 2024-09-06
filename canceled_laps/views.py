from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import CanceledLap
from .forms import CanceledLapForm


class CanceledLapsListView(ListView):
    model = CanceledLap
    template_name = 'canceledlap_list.html'
    context_object_name = 'canceledlaps'

    def get_queryset(self):
        queryset = super().get_queryset()

        ticket_locator = self.request.GET.get('ticket_locator')
        passenger_last_name = self.request.GET.get('passenger_last_name')
        client = self.request.GET.get('client')
        posted_by = self.request.GET.get('posted_by')

        if ticket_locator:
            queryset = queryset.filter(ticket_locator__icontains=ticket_locator)
        
        if passenger_last_name:
            queryset = queryset.filter(passenger_last_name__icontains=passenger_last_name)

        if client:
            queryset = queryset.filter(client__name__icontains=client)
        
        if posted_by:
            queryset = queryset.filter(posted_by__icontains=posted_by)

        return queryset


class CanceledLapsCreateView(CreateView):
    model = CanceledLap
    template_name = 'canceledlap_create.html'
    success_url = reverse_lazy('canceledlap_list')
    form_class = CanceledLapForm


class CanceledLapsDetailView(DetailView):
    model = CanceledLap
    template_name = 'canceledlap_detail.html'


class CanceledLapsUpdateView(UpdateView):
    model = CanceledLap
    template_name = 'canceledlap_update.html'
    success_url = reverse_lazy('canceledlap_list')
    form_class = CanceledLapForm


class CanceledLapsDeleteView(DeleteView):
    model = CanceledLap
    template_name = 'canceledlap_delete.html'
    success_url = reverse_lazy('canceledlap_list')

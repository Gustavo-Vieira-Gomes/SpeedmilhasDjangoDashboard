from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from airlines.models import Airline
from django.urls import reverse_lazy
from airlines.forms import AirlineForm


class AirlineListView(ListView):
    model = Airline
    template_name = 'airline_list.html'
    context_object_name = 'airlines'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AirlineCreateView(CreateView):
    model = Airline
    template_name = 'airline_create.html'
    success_url = reverse_lazy('airline_list')
    form_class = AirlineForm


class AirlineUpdateView(UpdateView):
    model = Airline
    template_name = 'airline_update.html'
    success_url = reverse_lazy('airline_list')
    form_class = AirlineForm


class AirlineDetailView(DetailView):
    model = Airline
    template_name = 'airline_detail.html'


class AirlineDeleteView(DeleteView):
    model = Airline
    template_name = 'airline_delete.html'
    success_url = reverse_lazy('airline_list')

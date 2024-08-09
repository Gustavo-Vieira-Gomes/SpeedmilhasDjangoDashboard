from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from cards.models import Card
from django.urls import reverse_lazy
from cards.forms import CardForm


class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'cards'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')

        owner = self.request.GET.get('owner')
        
        if name:
            queryset = queryset.filter(name__icontains=name)

        if owner:
            queryset = queryset.filter(owner__icontains=owner)

        return queryset


class CardCreateView(CreateView):
    model = Card
    template_name = 'card_create.html'
    success_url = reverse_lazy('card_list')
    form_class = CardForm


class CardUpdateView(UpdateView):
    model = Card
    template_name = 'card_update.html'
    success_url = reverse_lazy('card_list')
    form_class = CardForm


class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detail.html'


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card_delete.html'
    success_url = reverse_lazy('card_list')

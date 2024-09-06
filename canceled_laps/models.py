from django.db import models
from clients.models import Client
from cards.models import Card


STATUS_OPTIONS = [('A Cancelar', 'A Cancelar'), ('Cancelada', 'Cancelada'), ('Marcio', 'Marcio'), ('Daniel', 'Daniel'), ('Jessica', 'Jessica'), ('Revisando', 'Revisando')]


class CanceledLap(models.Model):
    emission_date = models.DateField()
    account_login = models.CharField(max_length=200)
    individual_cost = models.DecimalField(max_digits=11, decimal_places=2)
    tickets_number = models.IntegerField()
    individual_profit = models.DecimalField(max_digits=11, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='canceled_laps')
    posted_by = models.CharField(max_length=50)
    credit_card = models.ManyToManyField(Card, related_name='canceled_laps')
    total_selling_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    refunded_on_card = models.BooleanField(default=False)
    cancellation_cost = models.CharField(max_length=100, blank=True, null=True)
    payment_verified = models.BooleanField(default=False)
    ticket_locator = models.CharField(max_length=20)
    passenger_last_name = models.CharField(max_length=40, blank=True, null=True)
    cancellation_datetime = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS)
    annotations = models.TextField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=11, decimal_places=2)
    total_profit = models.DecimalField(max_digits=11, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.ticket_locator

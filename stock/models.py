from django.db import models
from accounts.models import Account
from airlines.models import Airline


class Stock(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='accounts')
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT, related_name='airline')
    annotation = models.TextField(blank=True, null=True)
    date = models.DateField()
    paid_miles = models.PositiveIntegerField(blank=True, null=True)
    origin = models.CharField(max_length=250, blank=True, null=True)
    owner = models.CharField(max_length=200)
    miles_price = models.FloatField(blank=True, null=True)
    current_miles_balance = models.IntegerField()
    due_date = models.DateField()
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.account__account_login

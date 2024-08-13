from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'airline', 'annotation', 'date', 'paid_miles', 'origin', 'owner', 'miles_price', 'current_miles_balance', 'due_date',)
    search_fields = ('account', 'airline', 'origin', 'owner',)


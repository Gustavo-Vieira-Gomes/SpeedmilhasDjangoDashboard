from django.contrib import admin
from .models import CanceledLap


@admin.register(CanceledLap)
class CanceledLapsAdmin(admin.ModelAdmin):
    list_display = ('id', 'emission_date', 'account_login', 'individual_cost', 'tickets_number', 'individual_profit', 'client', 'posted_by', 'total_selling_price', 'refunded_on_card', 'cancellation_cost', 'payment_verified', 'ticket_locator', 'passenger_last_name', 'cancellation_datetime', 'status', 'annotations', 'total_cost', 'total_profit', 'created_at', 'updated_at')
    search_fields = ('emission_date', 'account_login', 'posted_by', 'client', 'credit_card', 'ticket_locator', 'passenger_last_name', 'cancellation_datetime', 'status')

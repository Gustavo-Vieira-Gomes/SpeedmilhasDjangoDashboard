from django.contrib import admin
from accounts.models import Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'holder', 'account_login', 'password', 'holder_id', 'account_number', 'updated_at')
    search_fields = ('holder', 'account_login', 'account_number', 'holder_id')

from django.contrib import admin
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'description',)
    search_fields = ('name', 'owner',)
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('airlines.urls')),
    path('', include('clients.urls')),
    path('', include('cards.urls')),
    path('', include('accounts.urls')),
]

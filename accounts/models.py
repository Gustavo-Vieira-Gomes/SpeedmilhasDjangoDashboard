from django.db import models

# Create your models here.

class Account(models.Model):
    holder = models.CharField(max_length=200)
    account_login = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    holder_id = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['holder']

    def __str__(self) -> str:
        return self.account_login
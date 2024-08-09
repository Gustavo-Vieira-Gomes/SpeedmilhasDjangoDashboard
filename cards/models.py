from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['owner']

    def __str__(self) -> str:
        return self.name
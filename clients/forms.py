from django import forms
from clients.models import Client


class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':2})
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
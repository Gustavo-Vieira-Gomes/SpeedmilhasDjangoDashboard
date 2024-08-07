from django import forms
from airlines.models import Airline


class AirlineForm(forms.ModelForm):
    
    class Meta:
        model = Airline
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':2})
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
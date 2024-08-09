from django import forms
from cards.models import Card


class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['name', 'owner', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':2})
        }
        labels = {
            'name': 'Nome',
            'owner': 'Dono do Cartão',
            'description': 'Descrição'
        }
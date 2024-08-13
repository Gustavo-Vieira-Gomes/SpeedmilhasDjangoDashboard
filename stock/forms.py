from django import forms
from .models import Stock


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['account', 'airline', 'annotation', 'date', 'paid_miles', 'origin', 'owner', 'miles_price', 'current_miles_balance', 'due_date']
        widgets = {
            'account': forms.Select(attrs={'class': 'form-control'}),
            'airline': forms.Select(attrs={'class': 'form-control'}),
            'annotation': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'paid_miles': forms.NumberInput(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'miles_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_miles_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
        labels = {
            'account': 'Conta',
            'airline': 'Companhia Aérea',
            'annotation': 'Anotações sobre a conta',
            'date': 'Data de inclusão',
            'paid_miles': 'Quantidade de milhas pagas para utilização',
            'origin': 'Proveniencia',
            'owner': 'Dono da Conta',
            'miles_price': 'Custo das milhas (Especificar se for diferente)',
            'current_miles_balance': 'Saldo de Milhas no momento',
            'due_date': 'Data de vencimento',
        }
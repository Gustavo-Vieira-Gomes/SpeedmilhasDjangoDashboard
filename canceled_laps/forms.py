from typing import Any
from django import forms
from .models import CanceledLap


class CanceledLapForm(forms.ModelForm):

    class Meta:
        model = CanceledLap
        fields = ['emission_date', 'account_login', 'individual_cost', 'tickets_number', 'individual_profit', 'client', 'posted_by', 'credit_card', 'total_selling_price', 'refunded_on_card', 'cancellation_cost', 'payment_verified', 'ticket_locator', 'passenger_last_name', 'cancellation_datetime', 'status', 'annotations']
        widgets = {
            'emission_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'account_login': forms.TextInput(attrs={'class': 'form-control'}),
            'individual_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'tickets_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'individual_profit': forms.NumberInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'posted_by': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_card': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'total_selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'refunded_on_card': forms.CheckboxInput(),
            'cancellation_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_verified': forms.CheckboxInput(),
            'ticket_locator': forms.TextInput(attrs={'class': 'form-control'}),
            'passenger_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cancellation_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'annotations': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

        labels = {
            'emission_date': 'Data da Emissão:',
            'account_login': 'Número/Login da conta:',
            'individual_cost': 'Custo por CPF:',
            'tickets_number': 'Número de CPFs:',
            'individual_profit': 'Valor por CPF:',
            'client': 'Cliente:',
            'posted_by': 'Emitido por:',
            'credit_card': 'Cartão de Crédito Usado:',
            'total_selling_price': 'Valor total',
            'refunded_on_card': 'Reembolsado no Cartão?',
            'cancellation_cost': 'Custo do Cancelamento:',
            'payment_verified': 'Pagamento Verificado?',
            'ticket_locator': 'Localizador',
            'passenger_last_name': 'Sobrenome do Passageiro',
            'cancellation_datetime': 'Data de chegada/cancelamento:',
            'status': 'Status da Emissão:',
            'annotations': 'Observações',
        }

    def clean(self):
        cleaned_data = super().clean()

        individual_cost = cleaned_data['individual_cost']
        tickets_number = cleaned_data['tickets_number']
        individual_profit = cleaned_data['individual_profit']

        total_cost = individual_cost * tickets_number
        total_profit = individual_profit * tickets_number

        cleaned_data['total_cost'] = total_cost
        cleaned_data['total_profit'] = total_profit

        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.total_cost = self.cleaned_data.get('total_cost')
        instance.total_profit = self.cleaned_data.get('total_profit')

        if commit:
            instance.save()

            self.save_m2m()

        return instance
from django import forms
from accounts.models import Account


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['holder', 'account_login', 'password', 'holder_id', 'account_number']
        widgets = {
            'holder': forms.TextInput(attrs={'class': 'form-control'}),
            'account_login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'holder_id': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'holder': 'Titular',
            'account_login': 'Login',
            'password': 'Senha',
            'holder_id': 'Documento do Titular',
            'account_number': 'Número da Conta',
        }

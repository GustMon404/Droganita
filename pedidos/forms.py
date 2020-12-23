from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, Select, CheckboxInput

from .models import Pedido


class LoginForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'username',
                                                             'class': "form-control",
                                                             'placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'id': 'password',
                                                             'class': "form-control", 'placeholder': 'Senha'}))


class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('produto', 'descricao', 'marca', 'tipo', 'encomenda', 'falta')
        widgets = {
            'produto': TextInput(attrs={'type': 'text', 'id': 'produto',
                                        'class': "form-control",
                                        'placeholder': 'exemplo: Losartana'}),
            'descricao': TextInput(attrs={'type': 'text', 'id': 'Descricao',
                                          'class': "form-control",
                                          'placeholder': 'exemplo: 50mg 30cpr'}),
            'marca': TextInput(attrs={'type': 'text', 'id': 'marca',
                                      'class': "form-control",
                                      'placeholder': 'exemplo: Eurofarma'}),

            'tipo': Select(attrs={'type': 'text', 'id': 'situacao',
                                  'class': "form-control"}),
            'encomenda': CheckboxInput(attrs={'type': 'checkbox', 'id': 'encomenda',
                                              'value': 'True',
                                              'class': 'form-check-input'}),

            'falta': CheckboxInput(attrs={'type': 'checkbox', 'id': 'falta', 'value': 'True',
                                          'class': 'form-check-input'})
        }

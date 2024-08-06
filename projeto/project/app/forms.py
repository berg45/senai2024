from django import forms
from .models import Clients
from django.forms import ModelForm

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        #fields = "__all__"
        fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state", "updated_at", "deleted_at"]

    #name = forms.CharField(label='Nome', max_length=100)
    #cpf_cnpj = forms.CharField(label='CPF ou CNPJ', max_length=150)
    #rg_ie = forms.CharField(label='Rg ou IE',max_length=150)
    #zip_code = forms.CharField(label='CEP',max_length=11)
    #address = forms.CharField(label='Endereço',max_length=150)
    #neighborhood = forms.CharField(label='Bairro',max_length=150)
    #number = forms.CharField(label='Número',max_length=5)
    #city = forms.CharField(label='Cidade',max_length=30)
    #state = forms.CharField(label='Estado',max_length=3)
    
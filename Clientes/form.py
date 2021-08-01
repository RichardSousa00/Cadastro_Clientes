from django.forms import ModelForm
from .models import Novo_Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Novo_Cliente
        # Campos de informações que serão exibidos.
        fields = ['Nome', 'Email', 'Telefone','Endereco']
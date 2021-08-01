from django.db import models
from django.core.validators import RegexValidator

# Onde são inseridas as informações.
class Novo_Cliente(models.Model):
    # Informações, cada uma com seu tipo.
    Data = models.DateTimeField(auto_now_add=True)
    Nome = models.CharField(max_length=200)
    # Função própria do django para validar email.
    Email = models.EmailField(max_length=250)
    # Regex para validar telefone.
    # Formato - (11)98765-4321 ou (11)8765-4321
    Telefone = models.CharField(validators = [RegexValidator(regex="(\(\d{0,2}\)\d{4,5}\-\d{4})$",message=("Formato correto: (01)12345-6789 ou (01)2345-6789"))], max_length = 14)
    Endereco = models.CharField(max_length=250)

    # Printar o nome.
    def __str__(self):
        return self.Nome
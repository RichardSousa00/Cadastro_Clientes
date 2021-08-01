from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ClienteForm
from .models import Novo_Cliente
import datetime

# Onde será guardado os clientes e suas informações
def listagem(request):
    data = {}
    data["Clientes"] = Novo_Cliente.objects.all()
    return render(request, 'Clientes/listagem.html',data)

# Página de cadastro
def Cliente_novo(request):
    data = {}
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, "Clientes/form.html", data)

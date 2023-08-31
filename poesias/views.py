#  from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("HOME")


def contato_view(request):
    return HttpResponse("Página de Contatos")


def usuario_view(request, nome):
    return HttpResponse(f"Página do Usuário: {nome}")


def sobre_view(request):
    return HttpResponse("Informações sobre a Empresa")


def poesia1_view(request):
    return HttpResponse("Poesia 1")


def poesia2_view(request):
    return HttpResponse("Poesia 2")


def poesia3_view(request):
    return HttpResponse("Poesia 3")


def venda_view(request):
    return HttpResponse("Informações sobre Vendas:")


# Create your views here.

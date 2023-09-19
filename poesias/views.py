from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html")


def contato_view(request):
    return render(request, "contato.html")


def usuario_view(request, nome):
    return HttpResponse(f"Página do Usuário: {nome}")


def sobre_view(request):
    return render(request, "sobre.html")


def poesia1_view(request):
    return HttpResponse("Poesia 1")


def poesia2_view(request):
    return HttpResponse("Poesia 2")


def poesia3_view(request):
    return HttpResponse("Poesia 3")


def venda_view(request):
    return HttpResponse("Informações sobre Vendas:")


def blog_view(request):
    return HttpResponse("Blog")


# Create your views here.

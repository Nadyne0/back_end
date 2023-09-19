from django.shortcuts import render
from django.http import HttpResponse
from poesias.utils.fabrica import fazer_poema


def home_view(request):
    return render(request, "home.html")


def contato_view(request):
    return render(request, "contato.html")


def usuario_view(request, nome):
    return HttpResponse(f"Página do Usuário: {nome}")


def sobre_view(request):
    return render(request, "sobre.html")


# Tag If
def poema_detalhe(request):
    poema = fazer_poema()
    return render(request, "poema_detalhe.html", {"poema": poema})


# Tag For
def poema_lista(request):
    poema = [fazer_poema() for _ in range(5)]
    return render(request, "poema_lista.html", {"poema": poema})


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

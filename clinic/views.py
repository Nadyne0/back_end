from django.shortcuts import render

# from django.http import HttpResponse


def home_v_view(request):
    return render(request, "home_v.html")


def veterinarios_view(request):
    return render(request, "veterinarios.html")


def contato_v_view(request):
    return render(request, "contato_v.html")

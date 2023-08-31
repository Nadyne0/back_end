"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from poesias import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view),
    path("contato/", views.contato_view),
    path("usuario/<str:nome>/", views.usuario_view),
    path("sobre/", views.sobre_view),
    path("poesia1/", views.poesia1_view),
    path("poesia2/", views.poesia2_view),
    path("poesia3/", views.poesia3_view),
    path("vendas/", views.venda_view),
]

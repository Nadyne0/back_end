from django.urls import path
import poesias.views as views

urlpatterns = [
    path("", views.home_view),
    path("contato/", views.contato_view),
    path("usuario/<str:nome>/", views.usuario_view),
    path("sobre/", views.sobre_view),
    path("poesia1/", views.poesia1_view),
    path("poesia2/", views.poesia2_view),
    path("poesia3/", views.poesia3_view),
    path("vendas/", views.venda_view),
]

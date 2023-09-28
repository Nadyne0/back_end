from django.urls import path
import poesias.views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home_view),
    path("contato/", views.contato_view),
    path("usuario/<str:nome>/", views.usuario_view),
    path("sobre/", views.sobre_view),
    #
    path("poema_detalhe/", views.poema_detalhe),
    #
    path("poema_lista/", views.poema_lista),
    path("poesia1/", views.poesia1_view),
    path("poesia2/", views.poesia2_view),
    path("poesia3/", views.poesia3_view),
    path("vendas/", views.venda_view),
    path("/", views.blog_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

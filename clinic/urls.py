from django.urls import path
import clinic.views as views

urlpatterns = [
    path("home_v/", views.home_v_view),
    path("veterinarios/", views.veterinarios_view),
    path("contato_v/", views.contato_v_view),
]

from django.contrib import admin
import poesias.models as models

# from django.utils.html import mark_safe

admin.site.register(models.Categoria)
admin.site.register(models.Autor)
admin.site.register(models.Poesia)
admin.site.register(models.Venda)
admin.site.register(models.Livro)

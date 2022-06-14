from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobre_nome',
                    'telefone', 'categoria', 'mostrar')
    list_display_links = ['nome']
    search_fields = ('nome', 'sobre_nome')
    list_editable = ('telefone', 'mostrar')
    list_per_page = 15


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

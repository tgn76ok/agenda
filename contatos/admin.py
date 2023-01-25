from django.contrib import admin
from .models import Categoria,contato
# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','data_criacao', 'telefone' ,'mostra')
    list_display_links = ('id','nome')
    list_per_page =10
    search_fields =('nome','sobrenome','id')
    list_editable = ('telefone','mostra')
    
admin.site.register(Categoria)
admin.site.register(contato,ContatoAdmin)
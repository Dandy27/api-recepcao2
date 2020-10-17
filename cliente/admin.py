
from django.contrib import admin
from .models import Pessoa

admin.site.site_header = "Cadastro de Clientes"
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display=('nome', 'cpf', 'get_data_de_nascimento', 'phone', 'sexo', 'get_data')
    search_fields=('nome', 'cpf', 'data_de_nascimento', 'phone', 'sexo', 'data')
    list_filter = ('sexo', 'data', ) 
    date_hierarchy = 'data'


    def get_data(self, obj):
        if obj.data:
            return obj.data.strftime('%d/%m/%y')
    get_data.short_description = 'Data de Publicação'


    def get_data_de_nascimento(self, obj):
        if obj.data_de_nascimento:
            return obj.data_de_nascimento.strftime('%d/%m/%y')
    get_data_de_nascimento.short_description = 'Data de Nascimento'





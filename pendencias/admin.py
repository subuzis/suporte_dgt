from django.contrib import admin
from .models import PendenciaSuporte
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

class PendenciasAdmin(admin.ModelAdmin):
    readonly_fields = ('PID', 'criado_em', 'atualizado_em')##campos gerados automaticamente
    list_display = ('cidade','prioridade','descricao', 'ocorrencia', 'ordem_servico','observacao','status', 'criado_em') ##o que será mostrado na tela
    search_fields = ('cidade',) ##campo de pesquisa
    fields = ['cidade','prioridade','descricao','ocorrencia','ordem_servico','observacao','status', 'atualizado_em']#campos mostrados dentro da pendencia
    list_filter = ['status', 'author', 'criado_em', ('criado_em', DateRangeFilter)] ##filtro ao lado direito da tela
    pass
   
admin.site.register(PendenciaSuporte, PendenciasAdmin)
    

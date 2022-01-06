from django.contrib import admin
from .models import PendenciaSuporte

# Register your models here.

class PendenciasAdmin(admin.ModelAdmin):
    readonly_fields = ('PID', 'criado_em', 'atualizado_em')
    list_display = ('cidade','descricao','ordem_servico','ocorrencia','observacao','status', 'criado_em')
    search_fields = ('cidade',)
    fields = ['cidade','descricao','ordem_servico','ocorrencia','observacao','status', 'atualizado_em']
    
    
    pass
    
    


admin.site.register(PendenciaSuporte, PendenciasAdmin)
    

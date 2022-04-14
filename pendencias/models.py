
from django.db import models
from django.http import request
from django.urls import reverse_lazy


from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

LISTA_TECNICOS = (
    ('Davi', 'Davi Lobato'),
    ('Eduardo', 'Eduardo Palini'),
    ('Rita', 'Rita dos Santos'),
    ('Rua', 'Ruã Gonçalves'),
    ('Tiago', 'Tiago Cerveira'),)

# Create your models here.
class PendenciaSuporte(models.Model):
    

    

    cidadeslista = (
                ('DGT Base','DGT Base'),
                ('Alvorada','Alvorada'),
                ('Arroio Do Meio','Arroio Do Meio'),
                ('Bento Gonçalves','Bento Gonçalves'),
                ('Cachoeira do Sul','Cachoeira do Sul'),
                ('Cachoeirinha','Cachoeirinha'),
                ('Campo Bom','Campo Bom'),
                ('Candelaria','Candelaria'),
                ('Canguçu','Canguçu'),
                ('Canoas','Canoas'),
                ('Capela De Santana','Capela De Santana'),
                ('Charqueadas','Charqueadas'),
                ('Chuí','Chuí'),
                ('Cruz Alta','Cruz Alta'),
                ('Cuiabá','Cuiabá'),
                ('Cuiabá Fronteira','Cuiabá Fronteira'),
                ('Dois Irmãos','Dois Irmãos'),
                ('Encantado','Encantado'),
                ('Encruzilhada do Sul','Encruzilhada do Sul'),
                ('Espumoso','Espumoso'),
                ('Estancia Velha','Estancia Velha'),
                ('Esteio','Esteio'),
                ('Estrela','Estrela'),
                ('Gravatai','Gravatai'),
                ('Guaiba','Guaiba'),
                ('Harmonia','Harmonia'),
                ('Horizontina','Horizontina'),
                ('Ibirubá','Ibirubá'),
                ('Imbé','Imbé'),
                ('Irai','Irai'),
                ('Lagoa Vermelha','Lagoa Vermelha'),
                ('Lajeado','Lajeado'),
                ('Lindolfo Color','Lindolfo Color'),
                ('Mato Leitão','Mato Leitão'),
                ('Montenegro','Montenegro'),
                ('Não Me Toque','Não Me Toque'),
                ('Nova Petrópolis','Nova Petrópolis'),
                ('Nova Prata','Nova Prata'),
                ('Novo Hamburgo','Novo Hamburgo'),
                ('Pantano Grande','Pantano Grande'),
                ('Paraí','Paraí'),
                ('Parobé','Parobé'),
                ('Passo Fundo', 'Passo Fundo'),
                ('Porto Alegre','Porto Alegre'),
                ('Quarai','Quarai'),
                ('Rio Pardo','Rio Pardo'),
                ('Santa Cruz','Santa Cruz'),
                ('Santa Maria','Santa Maria'),
                ('Santa Vitória Do Palmar','Santa Vitória Do Palmar'),
                ('São Francisco de Paula','São Francisco de Paula'),
                ('São Leopoldo','São Leopoldo'),
                ('São Sepé','São Sepé'),
                ('Sapiranga','Sapiranga'),
                ('Sapucaia do Sul','Sapucaia do Sul'),
                ('Sobradinho','Sobradinho'),
                ('SSP','SSP'),
                ('Tramandaí','Tramandaí'),
                ('Três Coroas','Três Coroas'),
                ('UNIMED','UNIMED'),
                ('Vacaria','Vacaria'),
                ('Venâncio Aires','Venâncio Aires'),
                ('Vera Cruz','Vera Cruz'),)
    
    
    PID = models.AutoField(primary_key=True, unique=True)
    cidade = models.CharField(choices=cidadeslista, max_length=100)
    prioridade = models.CharField(choices=(
        ('a','Alta'),
        ('m','Media'),
        ('b','Baixa'),
    ),
        max_length=1,null=True,blank=False
    )
                                  
    descricao = models.CharField("Descricao", max_length=200,blank=False, null=False)
    ocorrencia = models.IntegerField("OC", blank=True, null=True)
    ordem_servico = models.IntegerField("OS", blank=True, null=True)
    observacao = models.TextField("Observacao", max_length=500,blank=True, null=True)
    status = models.CharField(choices=(
        ('pdgt','Pendente DGT'),
        ('ptp','Pendente Terceiro/Provedor'),
        ('pc','Pendente Cliente'),
        ('c','Concluido'),
        ('t','Tratando'),
    ),
        max_length=4
    )
    
    criado_em = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    atualizado_em = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    responsavel = models.CharField(choices=LISTA_TECNICOS, max_length=100, blank=False, null=True)
 
    ##11/01
    #image = models.ImageField(upload_to='pend_imgs', blank=True)
    


    class Meta:
        ordering = ['-criado_em'] ###ordenando por criados mais recentes
        verbose_name='pendencia'
        verbose_name_plural='pendencias'
        

          
    def __str__(self):
        """String for representing the Model object."""
        return f'Pendencia Nº{self.PID}' ##campo mostrado no topo da tela dentro da pendencia   



    


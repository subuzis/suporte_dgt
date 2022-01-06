from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class PendenciaSuporte(models.Model):
    cidadeslista = (        
                ('a','Alvorada'),
                ('b','Arroio Do Meio'),
                ('c','Bento Gonçalves'),
                ('d','Cachoeira do Sul'),
                ('e','Cachoeirinha'),
                ('f','Campo Bom'),
                ('g','Candelaria'),
                ('h','Canguçu'),
                ('i','Canoas'),
                ('j','Capela De Santana'),
                ('k','Charqueadas'),
                ('l','Chuí'),
                ('m','Cruz Alta'),
                ('n','Cuiabá'),
                ('o','Cuiabá Fronteira'),
                ('p','Dois Irmãos'),
                ('q','Encantado'),
                ('r','Encruzilhada do Sul'),
                ('s','Espumoso'),
                ('t','Estancia Velha'),
                ('u','Esteio'),
                ('v','Estrela'),
                ('y','Gravatai'),
                ('w','Guaiba'),
                ('z','Harmonia'),
                ('aa','Horizontina'),
                ('ab','Ibirubá'),
                ('qq','Imbé'),
                ('ww','Irai'),
                ('ss','Lagoa Vermelha'),
                ('zz','Lajeado'),
                ('cc','Lindolfo Color'),
                ('bb','Mato Leitão'),
                ('hh','Montenegro'),
                ('jj','Não Me Toque'),
                ('kk','Nova Petrópolis'),
                ('ll','Nova Prata'),
                ('oo','Novo Hamburgo'),
                ('pp','Pantano Grande'),
                ('ii','Paraí'),
                ('uu','Parobé'),
                ('yy','Porto Alegre'),
                ('tt','Quarai'),
                ('rr','Rio Pardo'),
                ('ee','Santa Cruz'),
                ('fr','Santa Maria'),
                ('fc','Santa Vitória Do Palmar'),
                ('fg','São Francisco de Paula'),
                ('fd','São Leopoldo'),
                ('sa','São Sepé'),
                ('sw','Sapiranga'),
                ('sd','Sapucaia do Sul'),
                ('sx','Sobradinho'),
                ('sz','SSP'),
                ('bv','Tramandaí'),
                ('bn','Três Coroas'),
                ('bg','UNIMED'),
                ('bh','Vacaria'),
                ('yu','Venâncio Aires'),
                ('kj','Vera Cruz'),)

    PID = models.AutoField(primary_key=True, unique=True)
    cidade = models.CharField(choices=cidadeslista,max_length=100)
    descricao = models.CharField("Descricao", max_length=200,blank=False, null=False)
    ordem_servico = models.IntegerField("OS", blank=True, null=True)
    ocorrencia = models.IntegerField("OC", blank=True, null=True)
    observacao = models.CharField("Observacao", max_length=200,blank=True, null=True)
    status = models.CharField(choices=(
        ('p','pendente'),
        ('c','concluido'),
        ('e','tratando'),
    ),
        max_length=1
    )
    
    criado_em = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    atualizado_em = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    
    class Meta:
        ordering = ['criado_em']
        verbose_name='pendencia'
        verbose_name_plural='pendencias'  

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.PID}'    



    


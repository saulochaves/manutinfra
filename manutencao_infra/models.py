# coding: utf-8 
from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# evolution =  manage.py evolve --hint -x

class Ordem(models.Model):
	class Meta:
		ordering = ('-datahora_criacao',)
	solicitante = models.CharField('Solicitante',max_length=40)
	setor = models.CharField('Setor',max_length=40)	
	descricao = models.TextField('Descrição da necessidade')
	datahora_criacao = models.DateTimeField('Data de Criação',default= datetime.now,editable=False)
	aguardando_aprovacao = models.BooleanField(default=True)
	criador = models.CharField(max_length=40, default = '' )
	modificado_por = models.CharField('Última modificação realizada por',max_length=40, default = '' )

class Ordem_Manutencao(Ordem):
	class Meta:
		verbose_name = "Ordem de Manutenção"
		verbose_name_plural = "Ordens de Manutenção"


	status_manutencao = (
		('em_aprovacao',u'EM APROVAÇÃO'),
		('aprovado',u'APROVADO'),
		('rejeitado',u'REJEITADO'),
		('cancelado',u'CANCELADO'),
		('em_execucao',u'EM EXECUÇAO'),
		('executado',u'EXECUTADO'),
			)

	status = models.CharField('Status da Solicitação',max_length = 20,choices = status_manutencao, default = 'em_aprovacao')
	equipamento = models.CharField('Equipamento',max_length=100)	
	
	
	def __str__(self):
		return str(self.id)

class Ordem_Infraestrutura(Ordem):
	class Meta:
		verbose_name = "Ordem de Infraestrutura"
		verbose_name_plural = "Ordens de Infraestrutura"

	status_infra = (
		('em_aprovacao',u'EM APROVAÇÃO'),
		('aprovado',u'APROVADO'),
		('rejeitado',u'REJEITADO'),
		('cancelado',u'CANCELADO'),
		('em_licitacao',u'EM LICITAÇÃO'),
		('em_execucao',u'EM EXECUÇAO'),		
		('executado',u'EXECUTADO'),
			)
	status = models.CharField('Status da Solicitação',max_length = 20,choices = status_infra, default = 'em_aprovacao')
	empresa = models.CharField('Empresa responsável pela obra/reparo',max_length=50)
	arquivo = models.FileField('Documentação de orçamento',upload_to = 'orcamentos',default='',blank = True)
	
	valor_orcamento = models.FloatField('Valor total do orçamento',default=0)

	def __str__(self):
		return str(self.id)




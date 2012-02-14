# coding: utf-8 
from django.contrib import admin
from models import Ordem , Ordem_Infraestrutura , Ordem_Manutencao
from django.contrib.auth.models import *
from django.contrib.auth.views import *
from django.contrib.admin import ModelAdmin
from views import *
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib import messages
from django import forms

class AdminManut(admin.ModelAdmin):
	ordering = ('-id',)
	list_display = ('id','solicitante','setor','datahora_criacao','status','criador','modificado_por')
	list_filter = ('solicitante','setor','status')	
	search_fields = ('id','solicitante','setor','status','criador','modificado_por')
	fields = ('solicitante','setor','equipamento','descricao','status')


	def save_model(self,request,obj,form,change):
		if obj.criador == '':
			obj.criador = request.user.username
			obj.save()
		else:
			if request.user.groups.filter(name= "Solicitante") :
				if  obj.status == "em_aprovacao" and obj.criador == request.user.username:
					obj.modificado_por = request.user.username	
					obj.save()
				else:
					return messages.error(request,"Você só pode modificar ordens criadas por você e com status 'EM APROVAÇÃO'. ")

			if request.user.groups.filter(name= "Aprovador") :
				status_aprovador = ['em_aprovacao','aprovado','rejeitado']
				if obj.status in status_aprovador:
					obj.modificado_por = request.user.username	
					obj.save()
				else :
					return messages.error(request,"Status inválido.")

			if request.user.groups.filter(name= "Gerente") :
				status_gerente = ['em_aprovacao','cancelado','em_execucao','executado']				
				if obj.status in status_gerente:
					obj.modificado_por = request.user.username	
					obj.save()
				else :
					return messages.error(request,"Status inválido.")
					


	def get_readonly_fields(self,request,obj=None):
		if request.user.groups.filter(name = 'Solicitante'):
			readonly_fields = ['status']
			return readonly_fields
		else:
			readonly_fields = ['solicitante','setor','equipamento','descricao']			
			return readonly_fields


		
class AdminInfra(admin.ModelAdmin):
	ordering = ('-id',)
	list_display = ('id','solicitante','setor','empresa','datahora_criacao','status','criador','modificado_por')
	list_filter = ('solicitante','setor','status','empresa')
	search_fields = ('id','solicitante','setor','status','empresa','criador','modificado_por')
	fields = ('solicitante','setor','empresa','descricao','status','valor_orcamento','arquivo')	


	def save_model(self,request,obj,form,change):
#### se o valor de criador for o default ('') , então criador recebe usuário logado		
		if obj.criador == '':
			obj.criador = request.user.username
			obj.save()
		else:
#### se o usuário logado é solicitante ele só pode modificar ordem criadas por ele e com status "EM APROVAÇÃO"
			if request.user.groups.filter(name= "Solicitante") :
				if  obj.status == "em_aprovacao" and obj.criador == request.user.username:
					obj.modificado_por = request.user.username	
					obj.save()
				else:
					return messages.error(request,"Você só pode modificar ordens criadas por você e com status 'EM APROVAÇÃO'. ")

#### se o usuário logado é gerente ele só pode aprovar, rejeitar ou voltar o status para "em aprovacao"
			if request.user.groups.filter(name= "Aprovador") :
				status_aprovador = ['em_aprovacao','aprovado','rejeitado']
				if obj.status in status_aprovador:
					obj.modificado_por = request.user.username	
					obj.save()
				else :
					return messages.error(request,"Status inválido.")

#### se o usuário logado é gerente, ele só pode definir os  status definidos em status_gerente
			if request.user.groups.filter(name= "Gerente") :
				status_gerente = ['em_aprovacao','cancelado','em_licitacao','em_execucao','executado']				
				if obj.status in status_gerente:
					obj.modificado_por = request.user.username	
					obj.save()
				else :
					return messages.error(request,"Status inválido.")

	def get_readonly_fields(self,request,obj=None):
		readonly_fields = []
		if request.user.groups.filter(name = 'Solicitante'):
			readonly_fields = ['status','valor_orcamento','arquivo']
#			return readonly_fields
		if request.user.groups.filter(name = 'Aprovador'):
			readonly_fields = ['solicitante','setor','empresa','descricao','valor_orcamento','arquivo']			
		if request.user.groups.filter(name = 'Gerente'):
			readonly_fields = ['solicitante','setor','descricao']
		return readonly_fields


admin.site.register(Ordem_Manutencao , AdminManut )
admin.site.register(Ordem_Infraestrutura , AdminInfra )

from piston.handler import BaseHandler
from manutinfra.manutencao_infra.models import Ordem_Manutencao , Ordem_Infraestrutura

class Handler_Manutencao (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Manutencao
	
	def read (self, request):
		ordens_manut = Ordem_Manutencao.objects.all()
		return ordens_manut

class Handler_Manutencao_ID (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Manutencao
	
	def read (self, request, ordem_id):
		ordens_manut = Ordem_Manutencao.objects.filter(id = ordem_id)			
		if ordens_manut == []:
			ordens_manut = "Nenhuma ordem encontrada"
		return ordens_manut

class Handler_Manutencao_Aprovacao (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Manutencao
	
	def read (self, request):
		ordens_manut_aprov = Ordem_Manutencao.objects.filter(status = 'em_aprovacao')
		if ordens_manut_aprov == []:
			ordens_manut_aprov = "Nenhuma ordem encontrada"
		return ordens_manut_aprov


class Handler_Infra (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Infraestrutura
	
	def read (self, request):
		ordens_infra = Ordem_Infraestrutura.objects.all()
		return ordens_infra


class Handler_Infra_ID (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Infraestrutura
	
	def read (self, request, ordem_id):
		ordens_infra = Ordem_Infraestrutura.objects.get(id = ordem_id)
		if ordens_infra == []:
			ordens_infra = "Nenhuma ordem encontrada"
		return ordens_infra

class Handler_Infra_Aprovacao (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Infraestrutura
	
	def read (self, request):
		ordens_infra_aprov = Ordem_Infraestrutura.objects.filter(status = 'em_aprovacao')
		if ordens_infra_aprov == []:
			ordens_infra_aprov = "Nenhuma ordem encontrada"
		return ordens_infra_aprov

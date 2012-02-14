#	def save(self,request,*args,**kwargs):
#		if self.status != 'em_aprovacao':
#			grupos = request.user.groups
#			for x in range(len(grupos)):
#				if grupos[x] == 'Aprovador' or request.user.is_superuser():
#					self.save()
#					break

#def verificar_usuario():
#	grupos = request.user.groups
#	if grupos[0] != 'Solicitante':
#			return True
#	else:
#		return False



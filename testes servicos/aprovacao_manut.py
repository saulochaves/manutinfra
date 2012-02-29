import urllib , json

ordens = urllib.urlopen('http://localhost:8000/api/ordens_manutencao/aprovacao')
ordens_formatadas = json.load(ordens)

if ordens_formatadas != "Nenhuma ordem encontrada":
	for x in range(len(ordens_formatadas)):
		if ordens_formatadas[x]['status'] == "em_aprovacao":
			print "Passou!"
		else:
			print "Erro!"
else:
	print "Nenhuma ordem encontrada"		

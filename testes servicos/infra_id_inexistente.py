import urllib, json

ordem = urllib.urlopen("http://localhost:8000/api/ordens_infraestrutura/99")
ordem_formatada = json.load(ordem)


if ordem_formatada == "Nenhuma ordem encontrada":
	print "Passou!"
else:
	print "Errado"

import urllib, json

ordem = urllib.urlopen("http://localhost:8000/api/ordens_infraestrutura/22")
ordem_formatada = json.load(ordem)


if ordem_formatada[0]['criador'] == 'solicitante':
	print "Passou!"
else:
	print "Errado!"

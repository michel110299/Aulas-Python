def eleicao():

	x = 10
	resultadoVotos = []
	votos = []
	menu = ['Digite 0 para parar a votação',
	'Digite 1, para votar no candidato A',
	'Digite 2, para votar no candidato B',
	'Digite 3, para votar no candidato C',
	'Digite 4, para votar nulo',
	'Digite 5, para votar em branco',
	'Digite 6 para ver apuração ']



	while x != 0:
		for lista in menu:
			print (lista)

		x = int(input("Digite sua opção:"))

		
		if x >=1 and x <=5:
			votos.append(x)
			print('Votação adicionada com sucesso!')
			print('\n\n\n')
			input()
		elif x >= 1 and x <= 6:
			if not votos:
				print('Não teve votos ainda')
				print('\n\n\n')
				input()
			else:
				Apuracao(votos)
		elif x == 0:
			print('fim')
			print('\n\n\n')
			input()
		else:
			print('Opção invalida!')
			print('\n\n\n')
			input()


def Apuracao(x):
	resultadoVotos = [0,0,0,0,0,0,0]
	cont = 0
	for v in x:
		cont += 1

		if v == 1:
			resultadoVotos[0] += 1
		elif v == 2:
			resultadoVotos[1] += 1
		elif v == 3:
			resultadoVotos[2] += 1
		elif v == 4:
			resultadoVotos[3] += 1
		elif v == 5:
			resultadoVotos[4] += 1

	print('Candidato 1 tem %s votos' %(resultadoVotos[0]))
	print('Candidato 2 tem %s votos' %(resultadoVotos[1]))
	print('Candidato 3 tem %s votos' %(resultadoVotos[2]))
	print('Votos nulos: %s ' %(resultadoVotos[3]))
	print('Votos em branco: %s' %(resultadoVotos[4]))
	if resultadoVotos[3] != 0:
		print('porcentagem de votos nulos sobre os votos: %s ' %((resultadoVotos[3]*100)/cont))
	if resultadoVotos[4] != 0: 
		print('porcentagem de votos brancos sobre os votos: %s ' %((resultadoVotos[4]*100)/cont))
	print('\n\n\n')

	resultadoVotos = []

	input()


		



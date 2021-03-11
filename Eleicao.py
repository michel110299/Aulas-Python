eleitores = []     
opcaoVoto=[] 
                                                                              
def eleicao():                                              

	x=10

	printar = [
	'|[0]- SAIR              |',
	'|[1]-CADASTRAR CANDIDATO|',
	'|[2]-CADASTRAR ELEITOR  |' ,
	'|[3]-VOTAR              |',
	'|[4]-APURAÇÃO DE VOTOS  |',
	'|[5]-LISTAR CANDIDATOS  |',
	'|[6]-LISTAR ELEITORES   |',
	'|[7]-PERCENTUAL DE VOTOS|'
	]


	while x!= 0:

		for aux in printar:
			print(aux)
		while True:
			try:
				x = int(input("Informe a sua opção:"))
				break
			except:
				print("Valor não e um inteiro insira novamente")
		if x == 0:
			print('FIM') 
		elif x == 1:
			while True:
				try:
					qtdCandidatos= int(input("Informe a quatidade de candidatos:"))
					break
				except:
					print("VALOR INVÁLIDO!")
			cadastro_canditados(qtdCandidatos)
		elif x == 2:
			cadastrarEleitores()
		elif x == 3:
			Votar()
		elif x == 4:
			Apuracaodevotos()
		elif x==5:
			Listarcandidatos()
		elif x == 6:
			ListarEleitores()
		elif x == 7:
			PercentualVotos()
		else:
			print('Opção invalida')


def cadastrarEleitores():
	while True:
			try:
				qtd_eleitores = int(input("Quantidades eleitores:"))
				break
			except:
				print("VALOR INVÁLIDO!")
	
	for cont in range(qtd_eleitores):
		nome =input("Nome do eleitor: ")
		while True:
			try:		
				cpf = int(input("Informe o seu CPF: "))
				break
				
			except:
				print("Valor não é um inteiro insira novamente")


		print("------------------------\n")
		if not eleitores:	
			eleitor = {
			    "nome": nome,
			    "cpf": cpf,
			}
			eleitores.append(eleitor)
		else:
			for e in eleitores:
				while e["cpf"]==cpf:
					aux = True
					while aux:
						try:		
							cpf = int(input("Informe o seu CPF: "))
							aux = False
							
						except:
							print("Valor não é um inteiro insira novamente")

			eleitor = {
			    "nome": nome,
			    "cpf": cpf,
			}
			eleitores.append(eleitor)

def cadastro_canditados(qtdCandidatos):

	if not opcaoVoto:
		branco = {
		"nome": "Voto branco",
		"qtdVotos": 0,
		}
		opcaoVoto.append(branco)

		nulo = {
			"nome": "Voto nulo",
			"qtdVotos": 0,
		}
		opcaoVoto.append(nulo)


	for cont in range(qtdCandidatos):

		nome = input("Nome do candidato: ")
		print("------------------------\n")
		candidato = {
		"nome": nome,
		"qtdVotos": 0,
		}
		opcaoVoto.append(candidato)


def Votar():
	if len(opcaoVoto) <= 1:
		print('Por favor! Insira mais de um candidato')
	elif not eleitores:
		print("Por favor! Insira eleitores")
	else:
		for e in range(len(eleitores)):
			cont = 1
			print("Eleitor - %s" %(e+1))
			for o in opcaoVoto:
				print("Pra votar '%s' digite: %s" % (o['nome'], cont))
				cont += 1



			voto = int(input("Digite sua opçao: "))

			while voto > len(opcaoVoto):

				voto = int(input("Digite sua opçao: "))




			opcaoVoto[voto-1]['qtdVotos'] += 1
			print("------------------------\n")


def Apuracaodevotos():

	if not opcaoVoto:
		print('Por favor! Insira um ou mais candidato')
	elif not eleitores:
		print("Por favor! Insira eleitores")
	else:
		for help in opcaoVoto:
			print(help["nome"])
			print(help["qtdVotos"])


def Listarcandidatos():
	if not opcaoVoto:
		print('Por favor! Insira um ou mais candidato')
	else:
		for aux in opcaoVoto:
			print(aux["nome"])

def ListarEleitores():
	if not eleitores:
		print('Por favor! Insira um ou mais eleitor')
	else:
		for aux in eleitores:
			print(aux["nome"])
			print(aux["cpf"])

def PercentualVotos():
	aux = 0
	for x in opcaoVoto:
		if x["qtdVotos"]>0:
			votoBranco = opcaoVoto[0]['qtdVotos']
			votoNulo = opcaoVoto[1]['qtdVotos']
			percentualBranco = (votoBranco*100)/len(eleitores)
			percentualNulo = (votoNulo*100)/len(eleitores)
			print('Percentual de votos branco foi de "%0.2f"' % percentualBranco)
			print('Percentual de votos nulo foi de "%0.2f"' % percentualNulo)
			aux = 1
			break
		else:
			aux=0
	if aux == 0:
		print('apuração de votos ainda não esta pronta')



	#1-Não aceitar string no cpf- FEITO
	#5-listar eleitor = FEITO
	#2-Não aceitar um candidato apenas = FEITO
	#4-Não aceitar o valor que não existe na eleição
	#3-CPF igual não aceitar = FEITO	
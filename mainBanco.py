from ClasseBanco import *
#all,
list = []

for a in range(1, 10):
	banco1 = bank()
	banco1.CriarConta(nome='michel',CPF = '140', nconta = '0205', id = 1)
	banco1.Depositar(a*10000)
	banco1.Sacar(1000)
	print(banco1.Saldo())

	list.append(banco1)



for a in list:
	print(a.nome)
	print(a.saldo)
	print(a.CPF)




#banco = bank.object.get(id = 1)






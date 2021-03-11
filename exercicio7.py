def mercado():
	valorMorango = 0 
	valorMaca = 0
	valorTotal = 0
	maca = 0
	morango = 0
	x = 3
	while x != 0:
		print('digite 0 para sair')
		print('digite 1 para comprar morango')
		print('digite 2 para comprar maçã')
		x = int(input('digite sua opção:'))

		if x == 1:
			morango = float(input('digite quantos kg de morango foi comprado'))
		elif x ==2:
			maca = float(input('digite quantos kg de maçã foi comprado'))
		elif x == 0:

			if (morango > 8) or ((morango*2.5) > 25):
				valorMorango = (morango*2.5)*0.9
			else:
				valorMorango = morango*2.5

			if (maca > 8) or (maca * 1.8)>25:
				valorMaca = (maca*1.8)*0.9
			else:
				valorMaca = maca*1.8

			print('Foi comprado %s kg de morango e o valor total foi %s R$' % (morango,valorMorango))
			print('Foi comprado %s kg de maca e o valor total foi %s R$' % (maca, valorMaca))
			print('O valor total foi %s R$' %(valorMorango+valorMaca) )
			print('Programa encerrado')		
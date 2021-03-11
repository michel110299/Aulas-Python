def triangulo(a,b,c):
	if (a+b)<c:
		print('È triangulo.')
	elif(a+c)<b:
		print('È triangulo.')
	elif(c+b)<a:
		print('È triangulo.')
	else:
		print('Não é um triangulo!')

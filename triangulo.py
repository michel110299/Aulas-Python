def triangulo(a,b,c):
	if (a+b)<c:
		print('triangulo')
	elif(a+c)<b:
		print('triangulo')
	elif(c+b)<a:
		print('triangulo')
	else:
		print('não é triangulo')
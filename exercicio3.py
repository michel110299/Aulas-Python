def fraseLonga(frase):

	f = frase 

	if len(frase) < 15:
		print(frase)
	else:
		frase = f[0:15]
		return frase + '...'
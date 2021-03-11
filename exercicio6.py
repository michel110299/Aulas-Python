import math
def baskara(a,b,c):
	delta=(b*b)-4*a*c

	if delta < 0:

		return 'raiz unica'  

	x1= -b+(math.sqrt(delta))/2*a
	x2= -b-(math.sqrt(delta))/2*a
	print(x1,x2)
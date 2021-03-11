class carro():
    def __init__(self, consumo, capacidade):
        self.cosumo = consumo
        self.capacidade = capacidade
        self.km = 0 
        self.tanque = 0 


    def mover(km):
    	if km >= self.km:
    		return 'não vai chegar meu caro'
    	self.km-=km
    	self.tanque-=km/self.consumo
    	return 'chegou ao seu destino'



    def abastecer(self, litros):
    	if self.capacidade < (self.tanque+litros):
    		return 'não cabe'

    	self.tanque+=litros
    	self.km = litros*self.consumo

    def gasolina():

    	return self.tanque

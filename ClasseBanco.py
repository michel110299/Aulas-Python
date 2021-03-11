class bank():

	def __init__(self):
		self.nome = ''
		self.CPF = ''
		self.nconta = ''
		self.saldo = 0 
		self.id = 0

	def CriarConta(self, nome, CPF, nconta,id):
		self.nome = nome
		self.CPF = CPF
		self.nconta = nconta
		self.id = id

	def Sacar(self, valorsaque):
		if valorsaque > self.saldo:
			print("SALDO INSUFICIENTE!")
		else:
			self.saldo -= valorsaque
			print('SAQUE REALIZADO COM SUCESSO!')

	def Depositar(self, valordeposito):
		self.saldo += valordeposito
		print('DEPÓSITO REALIZADO COM SUCESSO!')

	def Saldo(self):
		return self.saldo


		





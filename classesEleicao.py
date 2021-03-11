class Eleitores():
    def __init__(self):
        self.nome = ''
        self.CPF = ''
        self.id_eleitor = ''

    def CadastrarEleitor(self, nome, cpf, id_eleitor):
        self.nome = nome
        self.CPF = cpf
        self.id_eleitor = id_eleitor

    def ListarEleitor(self):
        print("Nome: %s" % (self.nome))
        print("CPF: %s" % (self.CPF))
        print("ID: %s" % (self.id_eleitor))


class Candidatos():
    def __init__(self):
        self.nome = ''
        self.nPartido = ''
        self.votos = 0

    def CadastrarCandidato(self, nome, nPartido):
        self.nome = nome
        self.nPartido = nPartido

    def ListarCandidato(self):
        print("Nome: %s" % (self.nome))
        print("Número partido: %s" % (self.nPartido))
        print("Votos: %s" % (self.votos))

    def Votar(self):
        self.votos += 1


class OpcDeVoto():
    def __init__(self):
        self.tipo = ''
        self.id = ''
        self.qtd_votos = 0

    def CadastrarOpcao(self, tipo, id_op):
        self.tipo = tipo
        self.id = id_op

    def Listarnulo(self):
        print("Tipo: %s" % (self.tipo))
        print("ID: %s" % (self.id))


def CadastroBranco():
    branco = OpcDeVoto()
    branco.CadastrarOpcao('branco', 1)
    return branco


def cadastroNulo():
    nullo = OpcDeVoto()
    nullo.CadastrarOpcao('nullo', 2)
    return nullo

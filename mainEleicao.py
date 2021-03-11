from classesEleicao import *
from random import randint

candidatos = []
eleitores = []
opcaoVoto = []


def main():

    x = 10

    opcaoVoto.append(CadastroBranco())
    opcaoVoto.append(cadastroNulo())

    lista = [
        '1 - CADASTRAR ELEITOR        ',
        '2 - MOSTRAR ELEITOR          ',
        '3 - CADASTRAR CANDIDATOS     ',
        '4 - MOSTRAR CANDIDATOS',
        '5 - para',
        '6 - para'
    ]

    while x != 0:
        for i in lista:
            print(i)

        while True:
            try:
                x = int(input("DIGITE UMA OPÇÃO: "))
                break
            except:
                print("DIGITE UM NUMERO INTEIRO CARAIO!!!!")

        if x == 0:
            print("fim")
        elif x == 1:
            CadastrarEleitor()
        elif x == 2:
            MostrarEleitores()
        elif x == 3:
            CadastrarCandidato()
        elif x == 4:
            ListarCandidatos()
        elif x == 5:
            print("ENTROU 5")
        elif x == 6:
            print("ENTROU ")

        else:
            print("OPÇÃO INVÁLIDA MEU CARO!")


def CadastrarEleitor():

    nome = input("digite o nome do eleitor")
    cpf = input("digite seu cpf")
    eleitor = Eleitores()
    eleitor.CadastrarEleitor(nome=nome, cpf=cpf, id_eleitor=gerarID())
    eleitores.append(eleitor)


def MostrarEleitores():

    for x in eleitores:
        print(x.ListarEleitor())


def CadastrarCandidato():
    nome = input("DIGITE NÚMERO DO PARTIDO:")
    nPartido = input("DIGITE NÚMERO DO PARTIDO:")

    candidato = Candidatos()

    candidato.CadastrarCandidato(nome=nome, nPartido=nPartido)
    candidatos.append(candidato)


def ListarCandidatos():
    for x in candidatos:
        print(x.ListarCandidato())


def gerarID():

    x = randint(0, 1000)

    for i in eleitores:
        while i.id_eleitor == x:
            x = randint(0, 1000)

    return x

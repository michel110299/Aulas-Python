# DESAFIO
# Fechar possiveis brechas pra erro.
# Adicionar o nome ao eleitor.
# Adicionar um menu se a pessoa quer cadastrar um candidato ou eleitor
# No menu tbm tem a opção de votar ou ver apuração de votos
# Dica coloque um campo no eleitor pra poder indicar quem vai votar


opcaoVoto = []
eleitores = 0
qtdCandidatos = 0


def eleicao():
    qtdCandidatos = int(
        input("Quantidade de canditos pra eleição: "))
    cadastro_canditados(qtdCandidatos)

    print("------------------------\n")
    eleitores = int(input("Quantidade de eleitores para votar: "))
    print("------------------------\n")

    for e in range(eleitores):
        cont = 1
        print("Eleitor - %s" % (e+1))
        for o in opcaoVoto:
            print("Pra votar '%s' digite: %s" % (o['nome'], cont))
            cont += 1

        voto = int(input("Digite sua opçao: "))
        opcaoVoto[voto-1]['qtdVotos'] += 1
        print("------------------------\n")

    for c in opcaoVoto:
        print("------------------------\n")
        print("Opção: %s" % c['nome'])
        print("Total de votos: %s" % c['qtdVotos'])
        print("------------------------\n")

    votoBranco = opcaoVoto[-2]['qtdVotos']
    votoNulo = opcaoVoto[-1]['qtdVotos']

    percentualBranco = (votoBranco*100)/eleitores
    percentualNulo = (votoNulo*100)/eleitores
    print('Percentual de votos branco foi de "%0.2f"' % percentualBranco)
    print('Percentual de votos nulo foi de "%0.2f"' % percentualNulo)


def cadastro_canditados(qtdCandidatos):

    for cont in range(qtdCandidatos):
        nome = input("Nome do candidato: ")
        print("------------------------\n")
        candidato = {
            "nome": nome,
            "qtdVotos": 0,
        }
        opcaoVoto.append(candidato)

    branco = {
        "nome": "Voto branco",
        "qtdVotos": 0,
    }
    opcaoVoto.append(branco)

    nulo = {
        "nome": "Voto nulo",
        "qtdVotos": 0,
    }
    opcaoVoto.append(nulo)

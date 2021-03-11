def CalcularIMC(altura , peso):               
    try:
        imc = peso/(altura*altura)
            
    except:
        print('ocorreu um erro!') 
            

    print(imc)

    if imc < 16:
        print('magreza grave')
    elif imc < 17:
        print('magreza moderada')
    elif imc < 18.5:
        print('magreza leve')
    elif imc < 25:
        print('saudável')
    elif imc < 30:
        print('sobrepeso')
    elif imc < 35:
        print('obesidade Grau |')
    elif imc < 40:
        print('obesidade Grau || (severa)')
    else:
        print('obesidade Grau ||| ()mórbida ')
  
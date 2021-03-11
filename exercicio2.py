def formatarNome(nome_completo):
	nome_formatado=[nome.capitalize()for nome in nome_completo.split()] 
	# nome.capitalize ele pega todas palavras e deixa a primeira letra em maiusculo
	# nome_completo.split() pega todos os espaço e joga tudo em um vetor 

	resultado = ' '.join(nome_formatado)  #join junta tudo que esta na lista uma string só 
	resultado = resultado.replace('Da','da').replace('De','de') # replace subistitui tudo que tem 'Da' por 'da' 
	return resultado 


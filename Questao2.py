import csv

####################################################################################
# Questão 2
#
# Function: busca_valor_endereco()
#
# Objetivo: saber o valor do endereço a partir dos comandos
#
# Execução: python Questao2.py
#
# Autor: Lucas Amarante - lucas.amarante42@gmail.com
####################################################################################

def busca_valor_endereco():
	valor_endereco = 0
	count = 0
	lista_encontrada = []

	file_commands = open('instructions/commands.txt', 'r')

	line_list = list(file_commands.readlines())

	i = 0
	while i < len(line_list):
		vend = line_list[i].strip()
		if '20' in vend:
			valor_endereco += int(vend[2:] or 0)
			count += 1
			lista_encontrada.append(vend)

		if vend[0] == '5':
			i += int(vend[1:] or 0)
			continue

		i += 1

	print('Foram encontrados {} registros e o valor do endereço é {}'.format(count, valor_endereco))

	#Cria arquivo planilha com o resultado
	with open('Out2.csv', 'w') as f:
		wr = csv.writer(f, delimiter="\n")
		wr.writerow(lista_encontrada)

busca_valor_endereco()
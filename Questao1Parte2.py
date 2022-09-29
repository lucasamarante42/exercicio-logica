from itertools import combinations
import csv

####################################################################################
# Questão 1 - Parte 2
#
# Function: senhas_em_regras()
#
# Objetivo: saber quantas combinações possíveis da senha podem
# 			existir usando algumas regras:
#	- A senha deve estar entre 184759-856920.
#	- Pelo menos dois dígitos adjacentes devem ser iguais (como 22 em 122346).
#	- Começando da esquerda para a direita, os dígitos só aumentam ou permanecem
# 	  os mesmos (como 111237 ou 135678).
#
# Execução: python Questao1Parte2.py
#
# Autor: Lucas Amarante - lucas.amarante42@gmail.com
####################################################################################

def senhas_em_regras():
	#Criação de lista combinada de números usando combinations do itertools
	lista_combinada = list(combinations(range(184759, 856920), 1))

	lista_valida = []

	for la in lista_combinada:
		a = str(la[0])

		proximo_eh_maior = True
		repete_duas_vezes = False

		#Verifica se próximo é maior
		for index, b in enumerate(a):
			if index == 0:
				if int(b) > int(a[index + 1]):
					proximo_eh_maior = False
					break

			elif index == 1:
				if int(b) < int(a[index]):
					proximo_eh_maior = False
					break

			elif index > 1:
				if int(b) < int(a[index - 1]):
					proximo_eh_maior = False
					break

		#Verifica números adjacentes
		counter = 0
		for index, c in enumerate(range(0, 5)):
			lista_separada = [a[index], a[index + 1]]

			if len(lista_separada) != len(set(lista_separada)):
				repete_duas_vezes = True
				counter += 1

		if proximo_eh_maior and repete_duas_vezes and counter >= 2:
			lista_valida.append(a)

	print('Existem {} senhas que seguem as regras de números próximos sempre maior e grupo de dois ou mais dígitos adjacentes!'.format(len(lista_valida)))
	# print(lista_valida)

	#Cria arquivo planilha com o resultado
	with open('Out-Part2.csv', 'w') as f:
		wr = csv.writer(f, delimiter="\n")
		wr.writerow(lista_valida)

senhas_em_regras()
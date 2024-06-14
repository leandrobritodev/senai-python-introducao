TITULO = 'Calculo de IMC'
# Autor: Leandro
# Data: 03/02/2024
# Descrição:
# Calcula o valor de IMC de uma pessoa.

print('Bem-vindo(a) ao programa ' + TITULO)
print('Este programa calcula o valor de IMC de uma pessoa.')
nome = input('Por gentileza informe seu nome: ')
cont_nome = str(len(nome))
idade = int(input('Agora informe sua idade: '))
ano_nasc = str(2024 - idade)
altura = float(input('Nos informe sua altura em centímetros: '))
peso = float(input('E por último seu peso em quilos: '))
imc = peso / altura ** 2
print('Seu nome é {} e tem {} caracteres, você tem {} anos e nasceu no ano de {}. Você mede {}cm, pesa {} Kg e seu '
      'IMC é: {}.'.format(nome, cont_nome, idade, ano_nasc, (altura * 100), peso, imc))

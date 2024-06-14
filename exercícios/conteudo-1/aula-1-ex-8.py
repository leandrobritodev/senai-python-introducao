TITULO = 'Descobrir ano futuro'
# Autor: Leandro
# Data: 03/02/2024
# Descrição:
# Descobre em qual ano o usuário descobre quando terá 80 anos.

print('Bem-vindo(a) ao programa ' + TITULO)
print('Este programa descobre em que ano você terá x anos. Você precisa informar '
      'sua idade atual, a idade que gostaria de descobrir e em que ano você está.')
idade_futura = int(input('Digite qual idade você gostaria de descobrir: '))
idade = int(input('Informe sua idade atual: '))
ano_atual = int(input('Digite o ano atual: '))
descobrir = idade_futura - idade
ano_futuro = ano_atual + descobrir
print('Em ' + str(ano_futuro) + ' você terá ' + str(idade_futura) + ' anos.')

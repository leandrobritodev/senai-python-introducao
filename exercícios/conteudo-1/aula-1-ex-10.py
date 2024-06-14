TITULO = 'Conversor de moedas'
# Autor: Leandro
# Data: 03/02/2024
# Descrição:
# Converte o valor informado em reais para dólares.

print('Bem-vindo(a) ao programa ' + TITULO)
print('Este programa converte o valor informado em reais para dólares')
reais = float(input('Informe o valor em reais: '))
dolares = reais / 5
print('A quantia de R${:.2f} corresponde ao valor de US${:.2f}'.format(reais, dolares))

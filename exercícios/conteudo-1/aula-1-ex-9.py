TITULO = 'Média de Notas'
# Autor: Leandro
# Data: 03/02/2024
# Descrição:
# Descobre a média de duas notas informadas pelo usuário.

print('''Bem-vindo(a) ao programa ' + TITULO)
Este programa descobre a média de duas notas informadas pelo usuário.''')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média das notas informadas é ' + str(media))

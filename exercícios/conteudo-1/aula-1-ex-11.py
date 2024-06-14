TITULO = 'Conversor de temperatura'
# Autor: Leandro
# Data: 03/02/2024
# Descrição:
# Converte a temperatura informada de Celsius para Fahrenheit.

print('Bem-vindo(a) ao programa ' + TITULO)
print('Este programa converte a temperatura informada de Celsius para Fahrenheit.')
print('Informe os graus em escala Celsius (°C):')
celsius = float(input())
fahrenheit = str((celsius * 1.8) + 32)
print('A temperatura {} °C corresponde à {} °F'.format(celsius, fahrenheit))

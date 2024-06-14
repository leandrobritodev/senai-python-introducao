import random
import time

print('''------------- Jogo de Dados --------------

Digite o número de vezes que será lançado dois dados
de seis lados (2D6).
Ao final será mostrado qual número que caiu mais.

------------------------------------------
''')
time.sleep(1)
lances = int(input('Digite quantos lances deseja: '))
resultado_2 = 0
resultado_3 = 0
resultado_4 = 0
resultado_5 = 0
resultado_6 = 0
resultado_7 = 0
resultado_8 = 0
resultado_9 = 0
resultado_10 = 0
resultado_11 = 0
resultado_12 = 0

for i in range(lances):
    dado_1 = random.randint(1,  6)
    dado_2 = random.randint(1, 6)
    soma = dado_1 + dado_2

    if soma == 2:
        resultado_2 += 1
    elif soma == 3:
        resultado_3 += 1
    elif soma == 4:
        resultado_4 += 1
    elif soma == 5:
        resultado_5 += 1
    elif soma == 6:
        resultado_6 += 1
    elif soma == 7:
        resultado_7 += 1
    elif soma == 8:
        resultado_8 += 1
    elif soma == 9:
        resultado_9 += 1
    elif soma == 10:
        resultado_10 += 1
    elif soma == 11:
        resultado_11 += 1
    elif soma == 12:
        resultado_12 += 1

print('2: ' + str(resultado_2))
print('3: ' + str(resultado_3))
print('4: ' + str(resultado_4))
print('5: ' + str(resultado_5))
print('6: ' + str(resultado_6))
print('7: ' + str(resultado_7))
print('8: ' + str(resultado_8))
print('9: ' + str(resultado_9))
print('10: ' + str(resultado_10))
print('11: ' + str(resultado_11))
print('12: ' + str(resultado_12))
time.sleep(2)

melhor_resultado = -1
melhor_numero = -1

if resultado_2 > melhor_resultado:
    melhor_resultado = resultado_2
    melhor_numero = 2
if resultado_3 > melhor_resultado:
    melhor_resultado = resultado_3
    melhor_numero = 3
if resultado_4 > melhor_resultado:
    melhor_resultado = resultado_4
    melhor_numero = 4
if resultado_5 > melhor_resultado:
    melhor_resultado = resultado_5
    melhor_numero = 5
if resultado_6 > melhor_resultado:
    melhor_resultado = resultado_6
    melhor_numero = 6
if resultado_7 > melhor_resultado:
    melhor_resultado = resultado_7
    melhor_numero = 7
if resultado_8 > melhor_resultado:
    melhor_resultado = resultado_8
    melhor_numero = 8
if resultado_9 > melhor_resultado:
    melhor_resultado = resultado_9
    melhor_numero = 9
if resultado_10 > melhor_resultado:
    melhor_resultado = resultado_10
    melhor_numero = 10
if resultado_11 > melhor_resultado:
    melhor_resultado = resultado_11
    melhor_numero = 11
if resultado_12 > melhor_resultado:
    melhor_resultado = resultado_12
    melhor_numero = 12

print('\nO maior resultado foi o {} com {} vezes '.format(melhor_numero, melhor_resultado))
print('Isto equivale a ' + str(melhor_resultado*100/lances) + ' %')

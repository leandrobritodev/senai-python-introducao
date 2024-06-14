import random

resultados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultados[dado1 + dado2 - 2] += 1


for indice, resultado in enumerate(resultados):
    print(f'{indice+2}: {resultado}')

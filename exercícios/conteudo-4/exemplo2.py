import random

resultados = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    dado = random.randint(1, 6)
    resultados[dado-1] += 1

for indice, resultado in enumerate(resultados):
    print(f'{indice+1}: {resultado}')
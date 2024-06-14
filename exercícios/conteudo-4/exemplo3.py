import random
dados = int(input('Digite o número de dados: '))
num_resultados = 5 * dados + 1
resultados = [0] * num_resultados

vezes = int(input('Digite o número de vezes que quer lançar o(s) dado(s): '))

for i in range(vezes):
    soma = 0
    for j in range(dados):
        soma += random.randint(1, 6)
    resultados[soma - dados] += 1

for indice, resultado in enumerate(resultados):
    print(f'{indice+dados}: {resultado}')
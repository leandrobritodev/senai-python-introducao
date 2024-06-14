cpf = input('Digite um CPF: ')

indice = 0
soma = 0
for numero in range(10, 1, -1):
    resultado = int(cpf[indice]) * numero
    print(f'{cpf[indice]} x {numero} = {resultado}')
    soma += resultado
    indice+= 1

print(f'Soma: {soma}')
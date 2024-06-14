def invertexto(nome):
    nome_invertido = ''
    for indice, letra in enumerate(nome):
        nome_invertido += nome[-indice - 1]
    return nome_invertido

nome = input('Digite o seu nome: ')
print(invertexto(nome))

def deslocar_palavras(texto, desloc=3):
    palavras = texto.split(' ')
    texto_deslocado = ''
    for palavra in palavras:
        if len(palavra) != 2:
            texto_deslocado += palavra[-desloc:] + palavra[:-desloc] + ' '
        else:
            texto_deslocado += palavra[::-1] + ' '
    return texto_deslocado[:-1]

print(deslocar_palavras('Aula de Python'))
print(deslocar_palavras(input('Digite um texto e, seguido de vírgula, o número de deslocamento: ')))
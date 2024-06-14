def substitui_letras(texto):
    substituicoes = {'A': '4', 'B': '8', 'E': '3', 'I': '1', 'O': '0', 'T': '7'}

    for letra, substituicao in substituicoes.items():
        texto = texto.replace(letra.upper(), substituicao)
        texto = texto.replace(letra.lower(), substituicao)
    return texto

texto = str(input('Digite seu texto: '))
texto_modificado = substitui_letras(texto)
print(texto_modificado)

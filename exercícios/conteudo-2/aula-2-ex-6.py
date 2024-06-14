print('''-------------------- Verificador de Ano Bissexto --------------------
Este programa verifica se um ano é bissexto ou não!
_________________________________________________________
''')
ano = int(input('Digite um ano: '))
if ano % 100 == 0 and ano % 400 == 0:
    if ano % 4 == 0:
        print('O ano {} é um ano bissexto.'.format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

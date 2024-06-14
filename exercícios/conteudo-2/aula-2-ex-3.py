print('''-------------------- Calculadora de Notas --------------------
Este programa calcula a média entre duas notas fornecidas e
verifica se o aluno está Aprovado, Reprovado ou em Recuperação!
_________________________________________________________
''')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media > 7:
    print('Sua média é {}. Você está APROVADO!'.format(media))
elif media < 5:
    print('Sua média é {}. Você está REPROVADO!'.format(media))
else:
    print('Sua média é {}. Você está em RECUPERAÇÃO!'.format(media))

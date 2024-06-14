print('''-------------------- Calculadora de Ajuste Salarial --------------------
Este programa calcula o ajuste salarial deste ano!
Observações: o ajuste varia de acordo com sua faixa salarial.
_________________________________________________________
''')
salario = float(input('Digite o seu salário atual em reais (R$): '))
if salario >= 5000:
    ajuste = (5 * salario) / 100
    print('Seu aumento é de 5%')
elif salario >= 3000 and salario <= 4999.99:
    ajuste = (10 * salario) / 100
    print('Seu aumento é de 10%')
elif salario >= 2000 and salario <= 2999.99:
    ajuste = ((15 * salario) / 100)
    print('Seu aumento é de 15%')
elif salario >= 1500 and salario <= 1999.99:
    ajuste = ((20 * salario) / 100)
    print('Seu aumento é de 20%')
else:
    ajuste = (25 * salario) / 100
    print('Seu aumento é de 25%')

novoSalario = salario + ajuste
print('''
O seu salário atual é de R${:.2f}
O aumento será de R${:.2f}
O salário após o reajuste será de R${:.2f}
    '''.format(salario, ajuste, novoSalario))


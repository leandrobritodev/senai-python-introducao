print('''-------------------- Calculadora de Desconto --------------------
Este programa calcula o desconto com base em sua idade.
Observação: O mínimo de desconto é 10% e o máximo é 80%.
_________________________________________________________
''')
VALOR_OCULOS = 200
idade = int(input('Digite a sua idade: '))
desconto = (VALOR_OCULOS * idade)/100
if idade >= 80:
    valor = VALOR_OCULOS - (80 * VALOR_OCULOS) /100
    print('Seu desconto é de 80%! O preço final ficará R${:.2f}'.format(valor))
elif idade <= 10:
    valor = VALOR_OCULOS - (10*VALOR_OCULOS) /100
    print('Seu desconto é de 10%! O preço final ficará R${:.2f}'.format(valor))
else:
    valor = VALOR_OCULOS - desconto
    print('Seu desconto é de {}%! O preço final ficará R${:.2f}'.format(idade, valor))
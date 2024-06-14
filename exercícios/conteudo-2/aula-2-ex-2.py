print('''-------------------- Nargets Ônibus --------------------
Oferecemos gratuidade no transporte para pessoas idosas.
Saiba se você se encaixa na categoria!
_________________________________________________________
''')
idade = int(input('Digite sua idade: '))
if idade >= 65:
    print('Parabéns! Você tem gratuidade no transporte!')
else:
    print('Infelizmente você não tem gratuidade no transporte :(')

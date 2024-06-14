import random
import time

print('------------- Jogo da Forca --------------')
time.sleep(1)
tentativas = 10
print('''\n***************************
   Tentativas Restantes
            {}
***************************\n'''.format(tentativas))
time.sleep(1)

palavra_1 = input('Digite a palavra n°1: ')
palavra_2 = input('Digite a palavra n°2: ')
palavra_3 = input('Digite a palavra n°3: ')
palavra_4 = input('Digite a palavra n°4: ')
palavra_5 = input('Digite a palavra n°5: ')
palavra_6 = input('Digite a palavra n°6: ')
palavra_7 = input('Digite a palavra n°7: ')
palavra_8 = input('Digite a palavra n°8: ')
palavra_9 = input('Digite a palavra n°9: ')
palavra_10 = input('Digite a palavra n°10: ')
numero_magico = (random.randint(1, 10))
palavra_chave = 'palavra_' + str(numero_magico)

for i in range(tentativas):
    print('Tentativa n°{}\n'.format(tentativas))
    tentativas -= 1
    palpite = input('Digite seu palpite: ')
    if palpite != (f"{palavra_chave}"):
        print('''Errou!
Tente novamente seu BURRO!!!!''')
        continue
    else:
        print('''Acertou!!!!
Você é muito inteligente sabia???''')
        break
else:
    print('A resposta certa era: {}'.format(palavra_chave))

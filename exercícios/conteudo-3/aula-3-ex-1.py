import random
import time

print('Adivinhe o número que o computador escolher')
time.sleep(1)
print('Você terá apenas 10 tentativas')
time.sleep(1)
tentativas = 1
numero_pc = random.randint(1, 1000)

while tentativas < 10:
    if tentativas < 10:
        numero = int(input('Digite um número de 1 a 1000: '))
        time.sleep(0.2)

        if numero < 1 and numero > 1000:
            print('Escolha um número dentro do escopo')
            time.sleep(0.2)
            continue

        if numero == numero_pc:
            print('Você acertou!!! O número é {}'.format(numero_pc))
            time.sleep(0.2)
            break

        elif numero < numero_pc:
            print('O número é maior que {}'.format(numero))
            time.sleep(0.2)
            tentativas += 1
            continue

        elif numero > numero_pc:
            print('O número é menor que {}'.format(numero))
            time.sleep(0.2)
            tentativas += 1
            continue
else:
    print('Errou o máximo de vezes')
    time.sleep(0.2)
    print('O número secreto era {}'.format(numero_pc))
    time.sleep(0.2)

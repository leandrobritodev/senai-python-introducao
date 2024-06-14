import random
import time

print('------------- TIC TAC TOE --------------')
time.sleep(1)
print('''Escolha uma opção:
(P) --> Papel
(R) --> Pedra
(T) --> Tesoura
(X) --> Sair''')
time.sleep(1)

num_vit = 0
num_der = 0

# ciclo do jogo
while True:
    # Sistema de Escolhas
    escolha_pc = random.randint(1, 3)
    escolha = input('Opção: ').upper()
    time.sleep(1)

    # Validação das escolhas
    if escolha not in ('P', 'R', 'T', 'X'):
        print('Opção inválida\n')
        time.sleep(1)
        continue
    elif escolha == 'X':
        print('''Encerrando o programa
----------------------------------------''')
        time.sleep(2)
        break

    if escolha == 'P' and escolha_pc == 2:
        print('Venceu! O sistema escolheu pedra.')
        time.sleep(1)
        num_vit += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'P' and escolha_pc == 3:
        print('Perdeu. O sistema escolheu tesoura.')
        time.sleep(1)
        num_der += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'P' and escolha_pc == 1:
        print('Empate!')
        time.sleep(1)
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    if escolha == 'R' and escolha_pc == 1:
        print('Venceu! O sistema escolheu papel.')
        time.sleep(1)
        num_vit += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'R' and escolha_pc == 3:
        print('Perdeu. O sistema escolheu tesoura.')
        time.sleep(1)
        num_der += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'R' and escolha_pc == 2:
        print('Empate!')
        time.sleep(1)
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    if escolha == 'T' and escolha_pc == 1:
        print('Venceu! O sistema escolheu papel.')
        time.sleep(1)
        num_vit += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'T' and escolha_pc == 2:
        print('Perdeu. O sistema escolheu pedra.')
        time.sleep(1)
        num_der += 1
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

    elif escolha == 'T' and escolha_pc == 3:
        print('Empate!')
        time.sleep(1)
        print('Vitórias: {} | Derrotas: {}'.format(num_vit, num_der))
        continue

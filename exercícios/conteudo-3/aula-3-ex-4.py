import random
import time

print('------------- Jogo de Luta --------------')
time.sleep(1)
vida_jogador = 10
vida_maquina = 10
print('''\n**********************
   Pontos de Vida
 Jogador  |  Máquina
   {}          {}
**********************\n'''.format(vida_jogador, vida_maquina))
time.sleep(1)

print('''Escolha uma opção:
(C) --> Cabeçada
(S) --> Soco
(X) --> Sair''')
time.sleep(1)

# ciclo do jogo
while True:
    # Sistema de Escolhas
    escolha_pc = random.randint(1, 3)

    escolha = input('\nOpção: ').upper()
    time.sleep(1)
    dado_pc = random.randint(1, 6)
    dado = random.randint(1, 6)

    # Validação das escolhas
    if escolha not in ('C', 'S', 'X'):
        print('Opção inválida\n')
        time.sleep(1)
        continue
    elif escolha == 'X':
        print('''\nEncerrando o programa
----------------------------------------''')
        time.sleep(2)
        break

# ------------------ HABILIDADE CABEÇADA ------------------

    if escolha == 'C' and dado_pc < 4:
        print('''Você escolheu usar a Cabeçada
Seu poder de combate é: 4
O poder de combate do inimigo é: {}\n'''.format(dado_pc))
        print('Acertou!')
        print('Você tira 3 de vida, recebe 1 de dano')
        vida_jogador -= 1
        vida_maquina -= 3
        print('''\n**********************
   Pontos de Vida
 Jogador  |  Máquina
   {}          {}
**********************\n'''.format(vida_jogador, vida_maquina))
        if vida_jogador <= 0:
            print('Você morreu! HAHAHAHAHAHAHAHAHAHAHA')
            break
        elif vida_maquina <= 0:
            print('Parabéns! Você ganhou!')
            break
    elif escolha == 'C' and dado_pc > 4:
        print('''Você escolheu usar a Cabeçada
Seu poder de combate é: 4
O poder de combate do inimigo é: {}\n'''.format(dado_pc))
        print('Errou!')
        print('Você recebe {} de dano'.format(dado_pc))
        vida_jogador -= dado_pc
        print('''\n**********************
   Pontos de Vida
 Jogador  |  Máquina
   {}          {}
**********************\n'''.format(vida_jogador, vida_maquina))
        if vida_jogador <= 0:
            print('Você morreu! HAHAHAHAHAHAHAHAHAHAHA')
            break
        elif vida_maquina <= 0:
            print('Parabéns! Você ganhou!')
            break

# ------------------ HABILIDADE SOCO ------------------

    elif escolha == 'S' and dado > dado_pc:
        print('''Você escolheu usar a Soco
Seu poder de combate é: {}
O poder de combate do inimigo é: {}\n'''.format(dado, dado_pc))
        print('Acertou!')
        print('Você tira {} de vida'.format(dado))
        vida_maquina -= dado
        print('''\n**********************
   Pontos de Vida
 Jogador  |  Máquina
   {}          {}
**********************\n'''.format(vida_jogador, vida_maquina))
        if vida_jogador <= 0:
            print('Você morreu! HAHAHAHAHAHAHAHAHAHAHA')
            break
        elif vida_maquina <= 0:
            print('Parabéns! Você ganhou!')
            break
    else:
        print('''Você escolheu usar a Soco
Seu poder de combate é: {}
O poder de combate do inimigo é: {}\n'''.format(dado, dado_pc))
        print('Errou!')
        print('Você recebe {} de dano'.format(dado_pc))
        vida_jogador -= dado_pc
        print('''\n**********************
   Pontos de Vida
 Jogador  |  Máquina
   {}          {}
**********************\n'''.format(vida_jogador, vida_maquina))
        if vida_jogador <= 0:
            print('Você morreu! HAHAHAHAHAHAHAHAHAHAHA')
            break
        elif vida_maquina <= 0:
            print('Parabéns! Você ganhou!')
            break

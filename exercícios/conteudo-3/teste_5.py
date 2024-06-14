senha = input('Digite a senha: ')
tentativas = 1

# while senha != 'a senha':
#     print('Senha incorreta, tente novamente')
#     senha = input()
# else:
#     print('Acesso liberado')

while senha != 'a senha':
    if tentativas < 3:
        tentativas += 1
        print('Senha incorreta')
        senha = input('Digite a senha: ')
    else:
        print('Acesso liberado')
        break
else:
    print('Errou o máximo de vezes')

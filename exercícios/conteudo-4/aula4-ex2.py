import time

print('------------- LISTA DE COMPRAS --------------')
time.sleep(1)
print('''Escolha uma opção:
(I) --> Inserir item
(E) --> Excluir item
(X) --> Sair''')
time.sleep(1)

lista_usuario = []
lista_compras = []

while True:
    escolha = input('Digite uma opção: ').upper()
    time.sleep(1)
    # Validação das escolhas
    if escolha not in ('I', 'E', 'X'):
        print('Opção inválida\n')
        time.sleep(1)
        continue
    elif escolha == 'X':
        print('''----------------------------------------
        Encerrando o programa
----------------------------------------
Sua lista de compras final: ''' + str(lista_compras))
        time.sleep(2)
        break
    if escolha == 'I':
        lista_usuario = input('Digite um item: ')
        lista_compras.append(lista_usuario)
        print('Lista de Compras: ' + str(lista_compras))
    elif escolha == 'E':
        print('Lista de Compras: ' + str(lista_compras))
        lista_usuario = input('Digite a ordem do item a ser excluído: ')
        lista_compras.pop(int(lista_usuario) - 1)
        print('Lista de Compras: ' + str(lista_compras))

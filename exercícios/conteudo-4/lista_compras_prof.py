titulo = 'Lista de Compras'
'''
Data: 29/04/2023
Autor: Daniel
Descrição: Cria uma lista com
a possibilidade de inserir
deletar e listar
'''
print('Seja bem vindo ao programa ' + titulo)

lista_de_compras = []

while True:
    print('''Escolha uma opção:
(I) --> Incluir
(M) --> Inclusão de Multiplos Itens
(D) --> Deletar
(L) --> Listar
(X) --> Sair''')
    escolha = input('Opção escolhida: ').upper()

    if escolha not in ('I', 'M', 'D', 'L'):
        print('Opção inválida')
        continue
    elif escolha == 'I':
        while True:
            item = input('Digite um item para incluir ou Q para sair: ').upper()
            if item == 'Q':
                break
            else:
                if item in lista_de_compras:
                    print('Item já foi incluido na lista')
                else:
                    lista_de_compras.append(item)
    elif escolha == 'M':
        lista_inclusao_txt = input("Digite os itens a ser incluidos com ',' separando: ")
        lista_inclusao = lista_inclusao_txt.split(',')
        for item_inclusao in lista_inclusao:
            lista_de_compras.append(item_inclusao.strip())
        #lista_de_compras.extend(lista_inclusao)
        print(f'Itens incluidos: ')
        for item in lista_inclusao:
            print(item,end=',')
        print()
    elif escolha == 'D':
        if len(lista_de_compras) > 0:
            print('Lista de Compras:')
            for indice, compra in enumerate(lista_de_compras, start=1):
                print(f'{indice} - {compra}')
            nr_item = int(input('Digite o número do item a ser deletado: '))
            item = lista_de_compras.pop(nr_item - 1)
            print(f'Item {item} deletado com sucesso')
        else:
            print('Lista de Compras Vazia')
    elif escolha == 'L':
        if len(lista_de_compras) > 0:
            print('Lista de Compras:')
            for indice, compra in enumerate(lista_de_compras, start=1):
                print(f'{indice} - {compra}')
        else:
            print('Lista de Compras Vazia')
    elif escolha == 'X':
        print('Saindo do programa')
        break
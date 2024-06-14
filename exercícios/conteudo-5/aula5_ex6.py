lista_usuarios = []

def cadastrar_usuario(nome, idade):
    usuario = {
        'nome': nome,
        'idade': idade
    }
    lista_usuarios.append(usuario)

cadastrar_usuario(nome='Daniel',idade=30)
cadastrar_usuario(nome=input('Digite o nome: '),idade=int(input('Digite a idade: ')))

# print(lista_usuarios)
for usuario in lista_usuarios:
    print(f'Nome: {usuario["nome"]:^15} | Idade: {usuario["idade"]:^4}')

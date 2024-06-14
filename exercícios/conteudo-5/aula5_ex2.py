def junta_nome():
    primeiro_nome = input('Digite o seu primeiro nome: ')
    segundo_nome = input('Digite o seu segundo nome: ')
    novo_apelido = primeiro_nome[:3] + segundo_nome[-3:]
    print('Seu novo apelido é: ' + str(novo_apelido))

junta_nome()
junta_nome()

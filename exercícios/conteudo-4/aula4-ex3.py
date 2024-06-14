cpf_usuario = input('Digite seu CPF(formato xxx.xxx.xxx-xx): ')
cpf_numeros = cpf_usuario.replace(".", "").replace("-", "")

if len(cpf_numeros) != 11:
    print('CPF inválido! Deve conter 11 números')
else:
    digitos_cpf = [int(digito) for digito in cpf_numeros]

    multiplicador = 10
    soma = 0
    for i in range(9):
        soma += digitos_cpf[i] * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - resto

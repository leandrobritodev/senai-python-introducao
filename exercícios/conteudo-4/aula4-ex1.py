nomes = ('''jose
jorge
maria
antonio
ana
julia
márcio
fernando
zelia'''.splitlines())


for indice, nome in enumerate(nomes):
    print(f'{indice + 1}°: {nome.title()}')

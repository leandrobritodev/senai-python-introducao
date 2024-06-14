import csv

def ler_arquivo(endereco):
    with open(endereco, 'r') as file:
        leitura = file.read()
    return leitura

def criar_csv(endereco, dados):
    with open(endereco, 'w', newline='') as file:
        writer = csv.writer(file)
        for linha in dados:
            writer.writerow(linha)

arquivo = ler_arquivo('Arquivos/alunos.txt')

lista_alunos = arquivo.split('\n')
lista_media = [['nome', 'nota 1', 'nota 2', 'media']]
for aluno in lista_alunos:
    campos_aluno = aluno.split(',')
    media = (float(campos_aluno[1]) + float(campos_aluno[2])) / 2
    campos_aluno.append(media)
    lista_media.append(campos_aluno)
print(lista_media)

criar_csv('Arquivos/alunos_media.csv', lista_media)
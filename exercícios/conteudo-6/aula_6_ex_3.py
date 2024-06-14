import csv

with open('Arquivos/alunos.txt', 'r') as file:
    arquivo = file.read()

lista_alunos = arquivo.split('\n')
lista_media = []
for aluno in lista_alunos:
    campos_aluno = aluno.split(',')
    media = (float(campos_aluno[1]) + float(campos_aluno[2])) / 2
    campos_aluno.append(media)
    lista_media.append(campos_aluno)
print(lista_media)

with open('Arquivos/alunos_media.csv', 'w', newline='') as file:
    header = ['nome', 'nota 1', 'nota 2', 'média']
    writer = csv.writer(file)
    writer.writerow(header)
    for aluno in lista_media:
        writer.writerow(aluno)
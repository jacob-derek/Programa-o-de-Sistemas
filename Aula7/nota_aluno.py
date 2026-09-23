""" Faça um programa que peça a nota de um aluno e informe se ele foi aprovado 
(nota maior ou igual a 7) ou reprovado. """

notas_aluno = []
media = 0

for notas in range(4):
    notas_aluno.append(float(input(f"Digite a nota número {notas + 1}: ")))

for nota in notas_aluno:
    media += nota

media = media / len(notas_aluno)

print(f"A sua média de notas é {media}.")

if media >= 7:
    print("Você está aprovado.")
else:
    print("Você está reprovado.")
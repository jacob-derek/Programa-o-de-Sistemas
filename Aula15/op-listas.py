from random import randint, choice

lista = []

for i in range(10):
    lista.append(randint(0, 10))

print(lista.sort())

while lista:
    remover = choice(lista)
    lista.remove(remover)
    print(lista)
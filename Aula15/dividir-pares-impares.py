from random import randint

todos_numeros = []
pares = []
impares = []

for i in range(20):
    todos_numeros.append(randint(0, 30))

print(sorted(todos_numeros))

for i, item in enumerate(todos_numeros):
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(sorted(pares))
print(sorted(impares))
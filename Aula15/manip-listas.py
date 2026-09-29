from random import randint
numeros = []

for i in range(10):
    numeros.append(randint(0, 20))

print(numeros)
print(numeros[-2])
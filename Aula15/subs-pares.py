from random import randint

pares  = []

for i in range(20):
    pares.append(randint(0, 50))

print(pares)
for i, item in enumerate(pares):
    if item % 2 == 0:
        pares[i] = 0

print(pares)
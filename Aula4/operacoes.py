from time import sleep

numero_a = int(input("Digite um número: "))
numero_b = int(input("Digite outro número: "))

print(numero_a + numero_b)
print(numero_a - numero_b)

print(numero_a * numero_b)
print(numero_a ** numero_b)

if numero_b == 0:
	print("Não é possível operar divisões, divisões inteiras e módulos pois é impossível dividir para 0.")
else:
	print(numero_a / numero_b)
	print(numero_a // numero_b)
	print(numero_a % numero_b)



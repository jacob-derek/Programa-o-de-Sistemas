from time import sleep
####################################################################
#pedir 4 notas e mostrar a media

sleep(0.4)
print("Agora, você irá digitar 4 números.")
nota_a = float(input("Nota 1: "))
sleep(0.4)
nota_b = float(input("Nota 2: "))
sleep(0.4)
nota_c = float(input("Nota 3: "))
sleep(0.4)
nota_d = float(input("Nota 4: "))

soma_das_notas = nota_a + nota_b + nota_c + nota_d
media_das_notas = soma_das_notas/4

sleep(0.4)
print(f"A média entre esses números equivale a {media_das_notas}")

#################################################################
#calcular a area de um quadrado

sleep(0.4)
print("Agora, vamos calcular a área de um quadrado.")
tamanho_a = int(input("Digite o tamanho do lado: "))
sleep(0.4)
print(f"A área do quadrado é {tamanho_a ** 2}")

#################################################################
#pedir dois numeros inteiros e um numero real

sleep(0.4)
numero_inteiro_a = int(input("Digite um número inteiro: "))
sleep(0.4)
numero_inteiro_b = int(input("Digite um número inteiro: "))
sleep(0.4)
numero_real = float(input("Digite um número real: "))
sleep(0.4)

# - calcule e mostre o produto do (dobro do primeiro) com (metade do segundo)
resultado_dobro_vezes_metade = (2*numero_inteiro_a)*(numero_inteiro_b/2)
sleep(0.4)

# - a soma do triplo do primeiro com o terceiro
resultado_triplo_somado = (3*numero_inteiro_a) + (numero_real)
sleep(0.4)

# - o terceiro elevado ao cubo
resultado_cubo = numero_real ** 3
sleep(0.4)

#resultados imprimidos
print(f"O produto do dobro do primeiro com metade do segundo {resultado_dobro_vezes_metade:.2f}")
print(f"A soma do triplo do primeiro com o terceiro {resultado_triplo_somado:.2f}")
print(f"O terceiro elevado ao cubo {resultado_cubo:.2f}")

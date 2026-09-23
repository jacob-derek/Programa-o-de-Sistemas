print("Olá! Vamos comparar dois números inteiros e saber sua ordem.")

numero_a = int(input("Digite um número inteiro: "))
numero_b = int(input("Digite outro número inteiro: "))

if numero_a > numero_b:
    print(f"O {numero_a} é maior {numero_b}")
elif numero_a < numero_b:
    print(f"O {numero_a} é menor {numero_b}")
elif numero_a == numero_b:
    print(f"O {numero_a} é igual {numero_b}")

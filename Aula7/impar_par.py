"""Escreva um programa em python que verifique se o número informar é ou não par """

user_numero = float(input("Digite um número: "))

if user_numero == 0:
    print(f"{user_numero} é neutro.")
elif user_numero % 2 == 0:
    print(f"O número {user_numero} é par.")
else:
    print(f"O número {user_numero} é impar.")

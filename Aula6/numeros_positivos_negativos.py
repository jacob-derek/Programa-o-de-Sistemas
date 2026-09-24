user_numero = float(input("Digite um número: "))

if user_numero == 0:
    print("0 é neutro.")
elif user_numero > 0:
    print("Seu número é positivo.")
elif user_numero < 0:
    print("Seu número é negativo.")

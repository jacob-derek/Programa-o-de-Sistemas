def somar(a, b):
    print(a+b)

def subtrair(a, b):
    print(a-b)
    
def multiplicar(a, b):
    print(a*b)

def dividir(a, b):
    if b == 0:
        print("Nao pode dividir pra zero")
    else:
        print(a/b)

user_a = input("Digite o primeiro algarismo: ")
user_b = input("Digite o primeiro algarismo: ")

operacao = int(input("""Qual operação voce quer executar?
1 - somar
2 - subtrair
3 - multiplicar
4 - dividir\n"""))

if operacao == 1:
    somar(user_a, user_b)
elif operacao == 2:
    subtrair(user_a, user_b)
elif operacao == 3:
    multiplicar(user_a, user_b)
elif operacao == 4:
    dividir(user_a, user_b)
else:
    print("numero incorrespondente")

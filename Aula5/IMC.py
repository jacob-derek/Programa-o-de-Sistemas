#atividade
#calcular imc via peso/altura^2

print("Cálculo de IMC")

user_peso = float(input("Digite o seu peso: "))
user_altura = float(input("Digite a sua altura: "))

print(f"Seu respectivo IMC é: {user_peso/(user_altura**2):.2f}")


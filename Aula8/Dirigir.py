user_idade = int(input("Quantos anos você tem?: "))
user_habilitacao = input("""
Você tem habilitação?: 
S/N: """).strip().upper()

if user_habilitacao == "S" and user_idade >= 18:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")
user_idade = int(input("Qual a sua idade? "))
user_titulo = input("""
Você tem o Título de Eleitor?
S/N
\n""").upper().strip()

if 70 > user_idade >= 18 and user_titulo == "S":
    print("Precisa votar.")
else:
    print("Não pode votar.")
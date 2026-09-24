user_idade = int(input("Quanto anos você tem?: "))
user_titulo = input("""
Você tem título de eleitor?
S/N:
\n""").strip().upper()

if user_titulo == "S":
    if 70 > user_idade >= 18:
        print("Precisa votar.")
    elif user_idade >= 16:
        print("Voto opcional.")
    else:
        print("Não pode votar.")
else:
    print("Não pode votar sem título.")
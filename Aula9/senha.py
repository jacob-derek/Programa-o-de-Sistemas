senha = "1234"

tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    senha_user = input("Digite a senha: ")
    if senha_user == senha:
        print("Bem-vindo.")
        break
    else:
        tentativas += 1
        tentativas_restantes = limite_tentativas - tentativas
        
        if tentativas_restantes > 0:
            print("Tente novamente.")
        else:
            print("Acesso bloqueado")

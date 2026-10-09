produtos = {
    "Arroz": 60,
    "Feijao": 50,
    "Ovos": 20,
    "Margarina": 40,
}

#print(estoque["produtos"]["arroz"])

while True:
    user_item = input("Que item voce procura?: ").strip().lower().capitalize()
    if user_item in produtos:
        print(f"O item esta disponivel, temos {produtos[user_item]} unidades")
    else:
        print("Produto nao listado.")
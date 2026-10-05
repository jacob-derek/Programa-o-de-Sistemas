from time import sleep

# gerenciar lista de compras antes de ir ao supermercado, adicionar item, visualizar lista, menu simples

lista_de_compras = []

def AdicionarItem():
    novo_item = input("Nome do novo item: ")
    lista_de_compras.append(novo_item)

def RemoverItem():
    print(f"Qual item deseja remover?\n{lista_de_compras}")
    item_remover = input("\n-> ")
    lista_de_compras.remove(item_remover)

def ListarItens():
    for item in range(len(lista_de_compras)):
        i = 1
        print(f"Item {i}: {lista_de_compras[item]}")
        i += 1
        sleep(0.5)

# greetings
print("Olá, bem-indo à lista de compras.")

while True:
    sleep(0.3)
    user_option = int(input(f"""
    
Selecione uma opção no menu de ações:
1 - Adicionar item
2 - Remover item
3 - Ver lista
4 - Sair \n"""))

    if user_option == 4:
        print("Boas compras!")
        sleep(1)
        break
    elif user_option == 3:
        if lista_de_compras == []:
            print("Lista vazia.")
            sleep(0.5)
        else:
            ListarItens()
    elif user_option == 2:
        if lista_de_compras == []:
            print("A lista está vazia.")
        else:
            RemoverItem()
    elif user_option == 1:
        AdicionarItem()
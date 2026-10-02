# gerenciar lista de compras antes de ir ao supermercado
# adicionar item
# visualizar lista
# menu simples
from time import sleep

lista_de_compras = []
print("Olá, bem-indo à lista de compras.")

while True:
    sleep(0.3)
    user_option = int(input(f"""
    
Selecione uma opção no menu de ações:
1 - Adicionar item
2 - Ver lista
3 - Sair \n"""))
    if user_option == 3:
        print("Boas compras!")
        sleep(1)
        break
    elif user_option == 2:
        if lista_de_compras == []:
            print("Lista vazia.")
            sleep(0.5)
        else:
            for item in range(len(lista_de_compras)):
                i = 1
                print(f"Item {i}: {lista_de_compras[item]}")
                i += 1
            sleep(0.5)
    elif user_option == 1:
        novo_item = input("Nome do novo item: ")
        lista_de_compras.append(novo_item)

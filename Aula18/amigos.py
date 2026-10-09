amigos = {
"Nomes" : ["Ednei","Edvan","Ednar","Eduardo","Ed"],
"Idades" : [12, 13, 10, 11, 9]
}

def MostrarAmigos():
    cont = 0
    
    for nome in amigos["Nomes"]:
        print(f"Nome: {nome}")
        print(f"Idade: {amigos["Idades"][cont]}")
        cont += 1
    
    print(f'Existem {len(amigos["Nomes"])} amigos.')

    return cont

def AdicionarAmigo(nome, idade):
    amigos["Nomes"].append(nome)
    amigos["Idades"].append(idade)

    return nome, idade

MostrarAmigos()
user_input = input("Quer adicionar mais amigos?\n S/N: ").strip().capitalize()

if user_input == "S":
    new_friend_name = input("Qual o nome do seu amigo? ")
    new_friend_age = int(input("Qual a idade dele? "))

    AdicionarAmigo(new_friend_name, new_friend_age)
    MostrarAmigos()
else:
    print("Txau.")
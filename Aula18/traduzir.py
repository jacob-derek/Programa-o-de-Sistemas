dicionario = {
    "Ola" : "Hello",
    "Garrafa": "Bottle",
    "Xadrez" : "Chess"
}

while True:
    user_word = input("Digite uma palavra Ola, Garrafa ou Xadrez): ")
    if user_word in dicionario.keys():
        print(dicionario[user_word])
    else:
        print("Unable to find results.")
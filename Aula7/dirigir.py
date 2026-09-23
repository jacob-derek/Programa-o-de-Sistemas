user_idade = int(input("Digite sua idade: "))
user_habilitacao = input("""

Você tem habilitacao?
S/N
\n""").upper().strip()

if user_idade >= 18 and user_habilitacao == "S":
    print("Pode dirigir!")
else:
    print("Não pode dirigir")
palavra = input("Escreva algo: ").strip()
letras = 0

for i in palavra:
    letras += 1

print(f"a palavra {palavra} tem {letras} letras")
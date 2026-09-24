from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + "This text is red!")
print(Back.GREEN + "This text has a green background!")
print(Style.DIM + "This text is dim!")
print(Fore.BLUE + Back.YELLOW + "Blue text on a yellow background!")

meu_nome = "Jacob Derek"

hobbie = "gosto de tocar guitarra"
print(f"Olá, mundo! Eu sou o {meu_nome} e {hobbie}")

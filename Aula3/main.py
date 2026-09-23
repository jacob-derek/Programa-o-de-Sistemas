#settando as variaveis pra aula
inteiro = 25
flutuante = 1.5
palavra = "isto é palavra"
logico = True

#fazendo um loop pra repetir tudo
import os
while True:
    os.system("cls" if os.name == "nt" else "clear")
    #minhas variaveis pessoais
    nome = str(input("Qual o seu nome?: "))
    idade = int(input("Qual a sua idade?: "))
    altura = float(input("Qual a sua altura?: "))
    checar_chuva = input("Está chovendo hoje? S ou N?\n").strip().upper()

    #traduzir
    if checar_chuva == "S":
        checar_chuva = "Sim"
    else:
        checar_chuva = "Falso"

    #colorir
    from colorama import init, Fore
    init(autoreset=True) #resetar pro branco pós colorir algo

    #exibição final
    print(f"""
    Oi, este é o questionário que o professor Everton pediu.
    Meu nome é {Fore.RED + nome}{Fore.RESET};
    Minha idade é {Fore.YELLOW + str(idade)}{Fore.RESET};
    Minha altura é {Fore.LIGHTBLUE_EX + str(altura)}{Fore.RESET};
    Está chovendo? {Fore.MAGENTA + checar_chuva}{Fore.RESET};
    """)

    # o professor disse que podia escrever tudo um dps do outro, mas fica mto feio
    from time import sleep

    sleep(5)
    os.system("cls" if os.name == "nt" else "clear")

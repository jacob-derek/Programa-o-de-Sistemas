import colorama
import os
from time import sleep

#init
colorama.init()
os.system("cls" if os.name == "nt" else "clear")

#cores
azul = colorama.Fore.LIGHTBLUE_EX
amarelo = colorama.Fore.LIGHTYELLOW_EX
amarelo_forte = colorama.Fore.YELLOW
branco = colorama.Fore.LIGHTWHITE_EX
cinza = colorama.Fore.LIGHTBLACK_EX
reset = colorama.Fore.RESET

#pegar nome, idade, printar bonitinho
nome = input(azul + "Qual o seu nome? " + branco)
idade = int(input(azul + "Qual a sua idade? " + branco))

#limpeza-----
sleep(0.6)
os.system("cls" if os.name == "nt" else "clear")

#checagem
if idade >= 18:
    pode_ser_preso = branco + "pode"
else:
    pode_ser_preso = branco + "não pode"

#transformando idade em string pra dar cor à ela
idade = amarelo + str(idade)

#imprimir
print(f"""
{amarelo}Olá, {nome}{amarelo}.
{amarelo}Você tem {idade}{amarelo}, então você {pode_ser_preso}{amarelo} ser preso.
{amarelo_forte}CUIDADO!
{reset}
""")


"""Faça um programa que pergunte em que turno você estuda.
Peça para digitar: M - Matutino V - Vespertino N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """
import os
from time import sleep

turnos_respostas = {

    "D": "Bom dia!",
    "V": "Boa tarde!",
    "N": "Boa noite!" 
}

while True:

     os.system("cls" if os.name == "nt" else "clear")

    turno_aluno = str(input("""
    Em que turno você estuda? 
    [D]iurno - [V]espertino - [N]oturno
    \n""")).upper().strip()
    
    if turno_aluno in turnos_resposta:
        print(turno_respostas[turno_aluno])
        break
    
    print("Valor inválido.")
    sleep(1)

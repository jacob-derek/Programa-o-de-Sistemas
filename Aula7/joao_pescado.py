"""
João Pescador, comprou um pc para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado (50kg)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

peso_pesca = float(input("Quantos quilos pescou hoje?: "))
peso_regulamento = 50
excesso = peso_pesca - peso_regulamento

multa = 4
if peso_pesca <= peso_regulamento:
    print("pagar porra nenhuma")
elif peso_pesca > peso_regulamento:
    multa *= excesso
    print(multa)

"""Cria um programa que simule um sistema de login simples, onde o usuário deve digitar um nome de usuário e senha, e
o programa deve verificar se estão corretos (use valores fixos para usuário e senha)."""
import json

with open("banco.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

while True:
    usuario = input("Login: ")
    senha = input("Senha: ")

    login_valido = False

    for conta in dados["usuarios"]:
        if conta["usuario"] == usuario and conta["senha"] == senha:
            login_valido = True
            break
    
    if login_valido:
        print("Logado.")
        break
    print("Usuario ou senha errados.")
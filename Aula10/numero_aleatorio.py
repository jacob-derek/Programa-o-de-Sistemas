from random import randint

rand_num = randint(0, 10)

user_num = int(input("Digite um numero entre 0 e 10: "))
if user_num == rand_num:
    print(f"O seu número {user_num} é igual ao da maquina {rand_num}")
else:
    print(f"O seu número {user_num} é diferente do da maquina {rand_num}")
from time import sleep

user_number = int(input("Digite um número: "))

while user_number >= 0:
    print(f"{user_number}")
    user_number -= 1 
    sleep(1)

print("cabou")

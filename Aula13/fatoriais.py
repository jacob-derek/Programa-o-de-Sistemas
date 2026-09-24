user_num = int(input("Digite um numero: "))

if user_num <= 0:
    print("maior que 0.")
else:
    for i in range (1, user_num+1):
        user_num *= i 
    
    print(user_num)


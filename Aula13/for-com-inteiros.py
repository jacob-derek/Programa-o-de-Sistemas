num_a = int(input("Digite um numero: "))
num_b = int(input("Digite outro numero: "))

if num_b < num_a:
    print("por favor, b precisa ser > que a.")

else:
    for i in range(num_a, num_b+1):
        print(i)

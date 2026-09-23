def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Erro: divisao por 0."

calculadora_menu = {
"1": somar,
"2": subtrair,
"3": multiplicar,
"4": dividir
}

while True:
    print("\n1: Somar │ 2: Subtrair │ 3: Multiplicar │ 4: Dividir │ 5: Sair")
    user_opcao = int(input("Qual das operações realizar?"))
    
    if user_opcao == 5:
        break
    
    for opcao in calculadora_menu:
        try:
            num1 = float(input("DIgite o primeiro número: "))
            num2 = float(input("DIgite o segundo número: "))
            
            acao_calculadora = calculadora_menu[opcao]
            resultado = acao_calculadora(num1, num2)
            
            print(f"Resultado: {resulatdo}")
        except ValueError:
            print("Digite apenas número validos.")
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
#calcular salario
#pegar ganho por hora, em um mes
#mostrar total do salario do mes

print("Vamos calcular seus ganhos líquidos!")
user_salario_hora = float(input("Quanto você ganha por hora, atualmente? R$"))
user_horas_trabalhadas = int(input("Quantas horas por dia você trabalha?: "))
user_dias_trabalhados = int(input("Quantos dias você trabalha por mês?: "))

user_salario_bruto = user_salario_hora * user_horas_trabalhadas * user_dias_trabalhados

#printar salario bruto
print(f"\nSeu salário bruto: R${user_salario_bruto}")

desconto_IR = user_salario_bruto * 0.11
desconto_INSS = user_salario_bruto * 0.08
desconto_SINDICATO = user_salario_bruto * 0.05

user_salario_liquido = user_salario_bruto - desconto_INSS - desconto_IR - desconto_SINDICATO

#exibir pagamento ao IR descontando 11%
print(f"Descontando o IR: R${desconto_IR}")
#exibir pagamento ao INSS, 8%
print(f"Desconto do INSS: R${desconto_INSS}")
#exibir pagamento ao sindicato, 5%
print(f"Desconto do sindicato: R${desconto_SINDICATO}")
#exibir salario liquido
print(f"Ao fim dos descontos, seu salario liquido é: R${user_salario_liquido}")

#sou dono de pizzaria e quero reciclar o codigo pra calcular faturamento bruto que verifique o valor de pizza quantidade de pizza vendida no mes
#deducao de custos 30%
#custos variados 20%
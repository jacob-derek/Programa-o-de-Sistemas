#faturamento da pizzaria
print("Vamos calcular o faturamento da pizzaria!")
preco_pizza = float(input("Quanto custa uma pizza, atualmente? R$"))
pizzas_vendidas = int(input("Quantas pizzas foram vendidas?: "))

entrada_vendas_totais = preco_pizza * pizzas_vendidas

#printar faturamento bruto
print(f"\nSeu faturamento bruto: R$ {entrada_vendas_totais:.2f}")

#deducao de custos fixos 30%
deducao_fixos = entrada_vendas_totais * 0.3

#custos custos variados 20%
deducao_variados = entrada_vendas_totais * 0.2

lucro_liquido = entrada_vendas_totais - deducao_fixos - deducao_variados
print(f"Ao fim das deduções, seu lucro liquido é: R${lucro_liquido}")

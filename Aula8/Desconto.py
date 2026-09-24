valor_compra = float(input("Quanto você gastou em compras?: R$"))
is_user_vip = input("""
Você é cliente vip?
S/N
\n""").strip().upper()

if valor_compra >= 100 or is_user_vip == "S":
    print(f"""
Você ganhou um desconto de 10%!
Novo valor a pagar: R${valor_compra * 0.9:.2f}
""")
else:
    print(f"""
Você não tem direito ao desconto.
Valor total a pagar: R${valor_compra:.2f}
""")

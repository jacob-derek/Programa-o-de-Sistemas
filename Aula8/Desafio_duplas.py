#precisa decidir se ativa o protocolo de pouso forçado pq o motor morreu
#pra pousar forçado a nave precisa ter 15% de combustivel disponivel
# E precisa que a atmosfera do planeta seja respiravel OU
# os tripulantes têm trajes em 100% de segurança

print("""
O computaor da nave precisa decidir pousar forçadamente.
Dê informações dos status gerais a seguir:""")

litros_combustivel = int(input("""
Qual a porcentagem de litros de combustível que a nave ainda tem?
1 - mais de 15%
2 - sem combustivel
\n"""))

trajes_tripulantes = input("""
Qual o nível de segurança dos trajes dos tripulantes?
1 - 100%
2 - menos de 100%
""")

atmosfera_respiravel = input("""
A atmosfera é respirável?
1 - Sim
2 - Não
""")

if litros_combustivel == 1 and trajes_tripulantes == 1 or atmosfera_respiravel == 1:
    print("Iniciando protocolo do Pouso.")
else:
    print("Pouso Abortado: Risco de Morte.")


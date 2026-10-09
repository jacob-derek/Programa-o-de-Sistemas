dicionario_alunos = {
"Jacob" : 1,
"Wallace" : 2,
"Everton" : 3
}

def iterarDicionarios(dicionario):
    print("Chaves:")
    for chaves in dicionario.keys():
        print(chaves)
    
    print("\nItens:")
    for item in dicionario.values():
         print(item)

iterarDicionarios(dicionario_alunos)

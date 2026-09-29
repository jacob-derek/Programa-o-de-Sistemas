from random import randint

media_todos_alunos = []

def Aluno(nome, nota1, nota2, nota3, nota4):
    print(nome)
    print("Notas: ", nota1, nota2, nota3, nota4)
    media = (nota1+ nota2 + nota3 + nota4)/4
    
    print("Média: ", media)
    media_todos_alunos.append(media)
    print("")

Aluno("Jurandir",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Marcos",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Carol",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Guilherme",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Jacob",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Miguel",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Bruno",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Breno",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Barbie",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
Aluno("Ken",  randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(media_todos_alunos)

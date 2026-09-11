qtd = int(input("Quantos alunos são na turma? "))

for i in range(qtd):
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    print("Média do", nome, "é:", media)

    if media >= 7:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado!")
nome = input("Nome Completo Do Aluno: ")
data_nascimento = input("Data De Nascimento: ")
n1 = float(input("Nota da primeira prova: "))
n2 = float(input("Nota da segunda prova: "))
n3 = float(input("Pontos Extras De Atividade: "))

media = (n1 + n2) / 2
if media >= 7:
    print("O aluno %s foi aprovado com media %.2f" % (nome, media))
else:
    print("O aluno %s foi reprovado com media %.2f" % (nome, media))
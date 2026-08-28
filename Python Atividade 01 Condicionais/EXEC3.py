nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

frequencia = float(input("Digite a frequencia do aluno (%): "))

atividades_entregues = int(input("Digite quantas atividades foram entregues: "))
atividades_total = int(input("Digite quantas atividades existem no total: "))

media = (nota1 + nota2 + nota3) / 3

porcentagem_atividades = (atividades_entregues / atividades_total) * 100

if frequencia < 75:
    resultado = "Reprovado por frequencia"
    motivo = "A frequencia ficou abaixo de 75%."

elif media < 5:
    resultado = "Reprovado por nota "
    motivo = "A media ficou abaixo de 5."

elif media >= 9 and frequencia >= 90 and atividades_entregues == atividades_total:
    resultado = "Aprovado com excelencia"
    motivo = "Todos os requisitos foram atendidos."

elif media >= 7 and frequencia >= 75 and porcentagem_atividades >= 70:
    resultado = "Aprovado"
    motivo = "Nao atende aos requisitos para aprovacao com excelencia."

elif media >= 5 and media < 7 and frequencia >= 75:
    resultado = "Recuperacao"
    motivo = "A media ficou entre 5 e 6,99."

else:
    resultado = "Reprovado"
    motivo = "Nao atendeu aos requisitos."

print("\n--- Resultado ---")
print("Media:", round(media, 2))
print("Frequencia:", frequencia, "%")
print("Atividades entregues:", round(porcentagem_atividades, 2), "%")
print("Resultado:", resultado)
print("Principal motivo:", motivo)
turma = {
    "2026001": {"nome": "Ana", "nota": 8.5},
    "2026002": {"nome": "Bruno", "nota": 6.0},
    "2026003": {"nome": "Carla", "nota": 9.2}
}

soma_notas = 0

for matricula, dados in turma.items():
    nome = dados["nome"]
    nota = dados["nota"]

    if nota >= 7.0:
        situacao = "Aprovado"
    else:
        situacaoo = "Reprovado"

    print(f"{nome} - Nota: {nota} - Situação: {situacao}")

    soma_notas += nota

media = soma_notas / len(turma)
print(f"Média geral: {media:.2f}")

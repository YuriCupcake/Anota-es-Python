idade = int(input("Digite a idade: "))
salario = float(input("Digite o salario: "))
divida = float(input("Digite o valor da divida: "))
tempo = int(input("Digite o tempo de emprego em meses: "))
valor = float(input("Digite o valor solicitado: "))
parcelas = int(input("Digite o numero de parcelas: "))

comprometimento = divida / salario
parcela = valor / parcelas
novo = comprometimento + (parcela / salario)

if idade >= 21 and idade <= 65 and salario >= 2500 and tempo >= 12 and comprometimento <= 0.30 and parcela <= salario * 0.25:
    resultado = "APROVADA"
    motivo = "Todos os criterios foram atendidos."

elif idade >= 21 and idade <= 65 and salario >= 2500 and tempo >= 6 and novo <= 0.50:
    resultado = "APROVADA COM RESTRICOES"
    motivo = "A solicitacao nao atende todos os criterios da aprovacao normal."

else:
    resultado = "REPROVADA"

    if idade < 21 or idade > 65:
        motivo = "Idade fora da faixa permitida."
    elif salario < 2500:
        motivo = "Salario menor que R$ 2500."
    elif tempo < 6:
        motivo = "Tempo de emprego menor que 6 meses."
    elif comprometimento > 0.30:
        motivo = "A divida atual passa de 30% do salario."
    elif parcela > salario * 0.25:
        motivo = "A parcela passa de 25% do salario."
    elif novo > 0.50:
        motivo = "O novo comprometimento passa de 50%."
    else:
        motivo = "Nao atende aos criterios."

print("\n===== ANALISE DE CREDITO =====")
print("Valor da parcela: R$", round(parcela, 2))
print("Comprometimento atual:", round(comprometimento * 100, 2), "%")
print("Novo comprometimento:", round(novo * 100, 2), "%")
print("Resultado:", resultado)
print("Motivo:", motivo)
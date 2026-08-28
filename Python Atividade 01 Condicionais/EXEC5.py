renda = float(input("Digite a renda mensal: R$ "))

moradia = float(input("Digite os gastos com moradia: R$ "))
alimentacao = float(input("Digite os gastos com alimentacao: R$ "))
transporte = float(input("Digite os gastos com transporte: R$ "))
saude = float(input("Digite os gastos com saude: R$ "))
educacao = float(input("Digite os gastos com educacao: R$ "))
lazer = float(input("Digite os gastos com lazer: R$ "))
dividas = float(input("Digite os gastos com dividas: R$ "))

total_despesas = moradia + alimentacao + transporte + saude + educacao + lazer + dividas

saldo = renda - total_despesas

comprometimento = (total_despesas / renda) * 100

porcentagem_dividas = (dividas / renda) * 100

if total_despesas > renda and saldo < renda * -0.20:
    situacao = "INSOLVENCIA"
    recomendacao = "E necessario diminuir as despesas e tentar negociar as dividas."

elif comprometimento > 85 or porcentagem_dividas > 35:
    situacao = "CRITICA"
    recomendacao = "E recomendado cortar gastos e diminuir as dividas."

elif comprometimento >= 70 and comprometimento <= 85:
    situacao = "ATENCAO"
    recomendacao = "E bom controlar os gastos e evitar novas dividas."

elif comprometimento <= 70 and porcentagem_dividas <= 20:
    situacao = "SAUDAVEL"
    recomendacao = "A situacao esta boa, mas continue controlando os gastos."

else:
    situacao = "ATENCAO"
    recomendacao = "E recomendado acompanhar melhor os gastos."

print("\n--- Diagnostico financeiro ---")
print("Total de despesas: R$", round(total_despesas, 2))
print("Saldo mensal: R$", round(saldo, 2))
print("Renda comprometida:", round(comprometimento, 2), "%")
print("Percentual gasto com dividas:", round(porcentagem_dividas, 2), "%")
print("Situacao:", situacao)
print("Recomendacao:", recomendacao)
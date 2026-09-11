valor = float(input("Valor da compra: R$ "))
max_parcelas = int(input("Máximo de parcelas: "))

for p in range(1, max_parcelas + 1):
    juros = valor * 0.02 * p # 2% de juros por mês
    total = valor + juros
    valor_parcela = total / p

    print(p, "x de R$", valor_parcela, "- Total: R$", total)
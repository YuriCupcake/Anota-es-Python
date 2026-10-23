vendas = {
    "Janeiro": 12500,
    "Fevereiro": 9800,
    "Março": 15300,
    "Abril": 11700,
    "Maio": 18400
}

total = sum(vendas.values())
media = total / len(vendas)

maior_mes = max(vendas, key=vendas.get)
menor_mes = min(vendas, key=vendas.get)

print(f"Total vendido: R$ {total:,.2f}")
print(f"Média mensal: R$ {media:,.2f}")
print(f"Maior venda: {maior_mes} - R$ {vendas[maior_mes]:,.2f}")
print(f"Menor venda: {menor_mes} - R$ {vendas[menor_mes]:,.2f}")

print("\nMeses acima da média:")

for mes, valor in vendas.items():
    if valor > media:
        print(mes)

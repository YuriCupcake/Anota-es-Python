saldo = float(input("Valor da dívida: R$ "))
juros = float(input("Juros mensal (ex: 0.02 para 2%): "))
parcela = float(input("Valor da parcela: R$ "))
meses_limite = int(input("Limite de meses: "))

mes = 0

while saldo > 0 and mes < meses_limite:
    mes = mes + 1
    saldo = saldo + (saldo * juros) # Aplica juros
    saldo = saldo - parcela          # Paga a parcela
    print("Mês", mes, "- Saldo restante: R$", saldo)

if saldo <= 0:
    print("Dívida quitada em", mes, "meses!")
else:
    print("O tempo acabou e a dívida não foi paga.")
salario = float(input("Digite o salario bruto: "))
dependentes = int(input("Digite a quantidade de dependentes: "))
previdencia = float(input("Digite o valor da previdencia: "))
pensao = float(input("Digite o valor da pensao: "))

deducao = dependentes * 250

total = previdencia + pensao + deducao

base = salario - total

if base < 0:
    print("As deducoes sao maiores que o salario.")
else:
    if base <= 2500:
        aliquota = 0
    elif base <= 3500:
        aliquota = 0.075
    elif base <= 5000:
        aliquota = 0.15
    elif base <= 7500:
        aliquota = 0.225
    else:
        aliquota = 0.275

    imposto = base * aliquota
    liquido = salario - imposto

    print("Salario bruto:", salario)
    print("Total de deducoes:", total)
    print("Base de calculo:", base)
    print("Aliquota:", aliquota * 100, "%")
    print("Imposto:", imposto)
    print("Salario liquido:", liquido)
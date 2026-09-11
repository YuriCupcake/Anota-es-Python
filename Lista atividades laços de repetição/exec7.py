qtd = int(input("Quantos vendedores são? "))

for i in range(qtd):
    nome = input("Nome do vendedor: ")
    vendas = float(input("Total em vendas: R$ "))

    # Calcula comissão simples
    if vendas <= 10000:
        comissao = vendas * 0.03
    else:
        comissao = vendas * 0.05

    print(nome, "ganhou R$", comissao, "de comissão.")
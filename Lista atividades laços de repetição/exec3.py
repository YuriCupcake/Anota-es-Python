estoque = 100

while True:
    print("\n1- Entrar | 2- Sair | 3- Ver Estoque | 4- Encerrar")
    opcao = input("Escolha: ")

    if opcao == "1":
        qtd = int(input("Quantidade para adicionar: "))
        if qtd > 0:
            estoque = estoque + qtd
        else:
            print("Valor inválido!")

    elif opcao == "2":
        qtd = int(input("Quantidade para retirar: "))
        if qtd > estoque:
            print("Não tem tudo isso no estoque!")
        else:
            estoque = estoque - qtd

    elif opcao == "3":
        print("Estoque atual:", estoque)

    elif opcao == "4":
        print("Estoque final:", estoque)
        break
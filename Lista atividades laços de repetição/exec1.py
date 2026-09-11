saldo = 1000

while True:
    print("1 - Saldo | 2 - Sacar | 3 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        print("Seu saldo é:", saldo)

    elif opcao == "2":
        saque = float(input("Quanto quer sacar? "))
        if saque <= saldo:
            saldo = saldo - saque
            print("Saque feito!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "3":
        print("Até logo!")
        break
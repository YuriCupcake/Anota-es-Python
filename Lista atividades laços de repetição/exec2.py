soma_notas = 0
qtd_notas = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))

    # Se for -1, encerra a digitação
    if nota == -1:
        break

    # Testa se a nota é válida
    if nota >= 0 and nota <= 10:
        soma_notas = soma_notas + nota
        qtd_notas = qtd_notas + 1
        print("Nota cadastrada!")
    else:
        print("Nota inválida! Digite um valor entre 0 e 10.")

# Relatório final depois que o loop para
if qtd_notas > 0:
    media = soma_notas / qtd_notas
    print("\n--- RESULTADO FINAL ---")
    print("Quantidade de notas válidas:", qtd_notas)
    print("Média do aluno:", media)
else:
    print("\nNenhuma nota válida foi digitada.")
produto = {
    "nome": "Notebook",
    "preco": 4500.00,
    "estoque": 12
}

chave = input("Digite a informação desejada: ")

valor = produto.get(chave, "Informação não encontrada.")

print(valor)

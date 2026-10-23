estoque = {
    "teclado": 15,
    "mouse": 20,
    "monitor": 8,
    "notebook": 5
}

estoque["webcam"] = 10
estoque["mouse"] = 25
estoque.pop("monitor")

for produto, quantidade in estoque.items():
    print(f"Produto: {produto} | Quantidade: {quantidade}")

total = sum(estoque.values())
print("Quantidade total:", total)

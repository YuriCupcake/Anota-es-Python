pop_a = float(input("População Cidade A: "))
pop_b = float(input("População Cidade B: "))
anos_limite = int(input("Anos para simular: "))

for ano in range(1, anos_limite + 1):
    pop_a = pop_a + (pop_a * 0.03) # Cresce 3% ao ano
    pop_b = pop_b + (pop_b * 0.015) # Cresce 1.5% ao ano

    print("Ano", ano, "- Cidade A:", int(pop_a), "| Cidade B:", int(pop_b))
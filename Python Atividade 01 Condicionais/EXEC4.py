peso = float(input("Digite o peso da encomenda: "))
distancia = float(input("Digite a distancia em km: "))
tipo = input("Digite o tipo de entrega (normal, expressa ou urgente): ")
assinante = input("O cliente e assinante? (sim/nao): ")
compra = float(input("Digite o valor da compra: R$ "))

taxa_peso = peso * 2.50
taxa_distancia = distancia * 0.30

frete = taxa_peso + taxa_distancia

adicional_entrega = 0

if tipo == "expressa":
    adicional_entrega = frete * 0.30

elif tipo == "urgente":
    adicional_entrega = frete * 0.60

frete = frete + adicional_entrega

adicional_peso = 0

if peso > 30:
    adicional_peso = 80
    frete = frete + 80

adicional_distancia = 0

if distancia > 500:
    adicional_distancia = 100
    frete = frete + 100

desconto = 0

if assinante == "sim":
    desconto = desconto + 15

if compra > 1000:
    desconto = desconto + 10

if desconto > 20:
    desconto = 20

valor_desconto = frete * (desconto / 100)

frete_final = frete - valor_desconto

# Verificando se o frete pode ser gratis
if assinante == "sim" and compra >= 2000 and tipo == "normal" and peso <= 10:
    frete_final = 0
    frete_gratis = "Sim"
else:
    frete_gratis = "Nao"

print("\n--- Calculo do frete ---")
print("Taxa por peso: R$", round(taxa_peso, 2))
print("Taxa por distancia: R$", round(taxa_distancia, 2))
print("Adicional da entrega: R$", round(adicional_entrega, 2))
print("Adicional por peso: R$", round(adicional_peso, 2))
print("Adicional por distancia: R$", round(adicional_distancia, 2))
print("Desconto:", desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Frete gratis:", frete_gratis)
print("Frete final: R$", round(frete_final, 2))
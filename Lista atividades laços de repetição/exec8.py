qtd = int(input("Quantos números quer digitar? "))

soma = 0
pares = 0

for i in range(qtd):
    num = int(input("Digite um número: "))
    soma = soma + num

    if num % 2 == 0:
        pares = pares + 1

print("Soma total:", soma)
print("Média:", soma / qtd)
print("Quantidade de pares:", pares)
candidato1 = 0
candidato2 = 0
candidato3 = 0

while True:
    print("\n1- Ana | 2- Bruno | 3- Carla | 0- Encerrar")
    voto = input("Digite seu voto: ")

    if voto == "1":
        candidato1 = candidato1 + 1
    elif voto == "2":
        candidato2 = candidato2 + 1
    elif voto == "3":
        candidato3 = candidato3 + 1
    elif voto == "0":
        break

print("\n--- RESULTADO ---")
print("Ana:", candidato1, "votos")
print("Bruno:", candidato2, "votos")
print("Carla:", candidato3, "votos")
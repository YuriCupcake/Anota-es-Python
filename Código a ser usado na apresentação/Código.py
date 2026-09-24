# Memória simulada
memoria = [0, 0, 0]

# Driver de dispositivo simulado
gpu_ligada = False

def driver_gpu(comando):
    global gpu_ligada

    if comando == "LIGAR":
        gpu_ligada = True

# Inicializa o dispositivo
driver_gpu("LIGAR")


# Programa que será executado
programa = [
    "MOV 0 5",
    "ADD 0 3"
]


# Interpretador
def interpretar(programa):
    for instrucao in programa:

        partes = instrucao.split()

        comando = partes[0]
        posicao = int(partes[1])
        valor = int(partes[2])

        if comando == "MOV":
            memoria[posicao] = valor

        elif comando == "ADD":
            memoria[posicao] += valor


# Executa o programa
interpretar(programa)


# Resultado
print("Status da GPU:", "Ativa" if gpu_ligada else "Inativa")
print("Estado final da memória:", memoria)
vetor = [64, 25, 12, 22, 11]

for i in range(len(vetor) - 1, 0, -1):
    for j in range(i):
        if vetor[j] > vetor[j + 1]:
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

print("Vetor ordenado:", vetor)

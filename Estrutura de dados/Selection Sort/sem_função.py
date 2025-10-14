vetor = [530, 42, 91, 57, 49]

for i in range(len(vetor) - 1):
    menor = i
    for j in range(i + 1, len(vetor)):
        if vetor[j] < vetor[menor]:
            menor = j
    aux = vetor[i]
    vetor[i] = vetor[menor]
    vetor[menor] = aux

print("Vetor ordenado:", vetor)


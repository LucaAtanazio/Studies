def bubbleSort(vet):
    for i in range(len(vet) - 1, 0, -1):
        for j in range(i):
            if vet[j] > vet[j + 1]:
                vet[j], vet[j + 1] = vet[j + 1], vet[j]
lista = [64, 25, 12, 22, 11]

bubbleSort(lista)
print("Lista ordenada:", lista)

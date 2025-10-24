def selectionSort(vet):
    for i in range(len(vet) - 1):
        menor = i
        for j in range(i + 1, len(vet)):
            if vet[j] < vet[menor]:
                menor = j
        # Troca os valores
        aux = vet[i]
        vet[i] = vet[menor]
        vet[menor] = aux
lista = [530, 42, 91, 57, 49]

selectionSort(lista)
print("Lista ordenada:", lista)


def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

print("Encontre o Número no Vetor Ordenado")
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
alvo = [14, 5]

for num in alvo:
    resultado = busca_binaria(numeros, num)
    if resultado != -1:
        print(f"{num} encontrado na posição {resultado}")
    else:
        print(f"{num} não encontrado")

       
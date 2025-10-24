
def buscar_elementos(lista, valor):
    if valor in lista:
        return f"{valor} esta em {lista}"
    else:
        return f"{valor} não existe em {lista}"
lista_ex = [1,2,6,8,3,5]
print(buscar_elementos(lista_ex, 5))
print(buscar_elementos(lista_ex, 20))

def maior_numero(lista_numero):
    maior = max(lista_numero)
    return f"O maior numero de {lista_numero} é {maior}"
lista_sua = [1,7,5,20,100,-5]
print(maior_numero(lista_sua))

def exibir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento}\t", end="")
        print()
minha_mat = [[3,7,8],
             [6,2,9],
             [5,7,9],
             [4,6,8]]
exibir_matriz(minha_mat)


def somar_coluna(matriz, indice_coluna):
    soma = 0
    for linha in matriz:
        if indice_coluna < len(linha):
            soma += linha[indice_coluna]
    return soma

matriz_notas = [[5, 4, 1],
                [2, 6, 8],
                [8, 7, 9]]
print(f"Soma da coluna 1: {somar_coluna(matriz_notas, 0)}")
print(f"Soma da coluna 2: {somar_coluna(matriz_notas, 1)}")
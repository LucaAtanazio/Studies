"""
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida.
"""

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        if i >= j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in matriz:
    print(linha)

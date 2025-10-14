"""
5. Implemente um programa capaz de gerar e imprimir uma matriz de tamanho 10 x
10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² - 1 se i = j;
A[i][j] = 4i³ - 5j² + 1 se i > j;
"""

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            val = 2*i + 7*j - 2
        elif i == j:
            val = 3*i**2 - 1
        elif i > j:
            val = 4*i**3 - 5*j**2 + 1
        linha.append(val)
    matriz.append(linha)

for linha in matriz:
    print(linha)


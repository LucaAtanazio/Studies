"""
8. Entrar com valores inteiros para uma matriz A4x4 e para uma matriz B4x4. Gerar e
imprimir a SOMA (A+B).
"""

A = []
B = []
soma = []

for i in range(4):
    linha_A = []
    linha_B = []
    for j in range(4):
        linha_A.append(int(input(f"A[{i}][{j}]: ")))
    A.append(linha_A)

for i in range(4):
    linha_B = []
    for j in range(4):
        linha_B.append(int(input(f"B[{i}][{j}]: ")))
    B.append(linha_B)

for i in range(4):
    linha_soma = []
    for j in range(4):
        linha_soma.append(A[i][j] + B[i][j])
    soma.append(linha_soma)

for linha in soma:
    print(linha)

"""
3. Implemente um programa que verifique se uma matriz 2 x 3 é simétrica, ou seja,
se é igual à sua transposta. Ao final, retorne se a matriz é transposta ou não.
"""

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []
for j in range(3):
    linha_t = []
    for i in range(2):
        linha_t.append(matriz[i][j])
    transposta.append(linha_t)

simetrica = True
if len(matriz) != len(transposta) or len(matriz[0]) != len(transposta[0]):
    simetrica = False
else:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != transposta[i][j]:
                simetrica = False
                break

print("É simétrica?" if simetrica else "Não é simétrica.")

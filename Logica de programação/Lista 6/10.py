"""
10. Criar um algoritmo que entre com
valores inteiros para uma matriz m
3 x 3 e imprima a matriz final,
conforme mostrado a seguir:
[[1 2 3], [4 5 6], [7 8 9]] a matriz gira 270° [[3 6 9], [2 5 8], [1 4 7]]
"""

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

rotacionada = []
for j in range(2, -1, -1):
    nv_linha = []
    for i in range(3):
        nv_linha.append(matriz[i][j])
    rotacionada.append(nv_linha)

for linha in rotacionada:
    print(linha)

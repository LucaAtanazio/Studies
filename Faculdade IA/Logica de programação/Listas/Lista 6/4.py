"""
4. Implemente um programa que calcule a soma dos elementos de cada linha e
coluna de uma matriz e armazene os resultados em vetores. Ao final, exiba o valor
do somatório das linhas e das colunas armazenados nos vetores.
"""

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

somas_linhas = [0, 0, 0]
somas_colunas = [0, 0, 0]

for i in range(3):
    for j in range(3):
        somas_linhas[i] += matriz[i][j]
        somas_colunas[j] += matriz[i][j]

print("Somas das linhas:", somas_linhas)
print("Somas das colunas:", somas_colunas)

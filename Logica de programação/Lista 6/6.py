"""
6. Implemente um programa que leia uma matriz 5 x 5 e um valor X. O programa
deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização
(linha e coluna) do elemento ou uma mensagem de “elemento não encontrado”.
"""

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(i * 5 + j)
    matriz.append(linha)


X = int(input("Digite o valor para buscar: "))
encontrado = False

for i in range(5):
    for j in range(5):
        if matriz[i][j] == X:
            print(f"Encontrado na linha {i}, coluna {j}")
            encontrado = True
if not encontrado:
    print("Elemento não encontrado.")

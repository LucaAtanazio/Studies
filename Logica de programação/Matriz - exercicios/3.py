"""
3. Implemente um programa que verifique se uma matriz 2 x 3 é simétrica, ou seja,
se é igual à sua transposta. Ao final, retorne se a matriz é transposta ou não. 

não faça o codigo, explique o conceito
"""
print("Digite os valores da matriz 2x3:")
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []
for j in range(3):
    nova_linha = []
    for i in range(2):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

print("\nMatriz original (2x3):")
for linha in matriz:
    print(linha)

print("\nMatriz transposta (3x2):")
for linha in transposta:
    print(linha)
  
if matriz == transposta:
    print("\nA matriz é igual à sua transposta (impossível para 2x3!)")
else:
    print("\nA matriz NÃO é igual à sua transposta (como esperado para 2x3)")



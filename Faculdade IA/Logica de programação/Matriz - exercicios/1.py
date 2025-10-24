"""
1. Implemente um programa que calcule e retorne a soma dos elementos de uma
matriz 5 x 5 de números inteiros.
"""
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f"Posição {i},{j}: ")))
    matriz.append(linha)
    
soma_total = sum(sum(linha) for linha in matriz)
print(f"\nSoma total da matriz = {soma_total}")


"""
matriz1 = []
valor = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(valor)
        valor += 1
    matriz1.append(linha)
    
    
alunos = []
for i in range(3):
    print(f"\nAluno {i+1}:")
    notas = []
    for j in range(3):
        notas.append(float(input(f"Nota {j+1}: ")))
    alunos.append(notas)
     
"""
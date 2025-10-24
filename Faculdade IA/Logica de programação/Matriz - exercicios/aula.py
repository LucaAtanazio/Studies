"""1. Preencha uma matriz 3x3 com valores de 1 a 9 em ordem
crescente.
"""

matriz1 = []
valor = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(valor)
        valor += 1
    matriz1.append(linha)

print("\nMatriz 3x3 com valores de 1 a 9:")
for linha in matriz1:
    print(linha)


"""
2. Preencha uma matriz 4x4 com números pares começando de 2.
"""

matriz2 = []
valor = 2
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(valor)
        valor += 2
    matriz2.append(linha)

print("\nMatriz 4x4 com números pares:")
for linha in matriz2:
    print(linha)
    
"""
3. Preencha uma matriz 5x5 com valores aleatórios entre 0 e 100.
"""
import random

matriz3 = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz3.append(linha)

print("\nMatriz 5x5 com valores aleatórios:")
for linha in matriz3:
    print(linha)
    
"""
4. Implemente um algoritmo para calcular e imprimir a média de
cada aluno em uma classe de 3 alunos com 3 provas por aluno,
as notas devem ser lidas a partir do usuário.
"""  
alunos = []
for i in range(3):
    print(f"\nAluno {i+1}:")
    notas = []
    for j in range(3):
        notas.append(float(input(f"Nota {j+1}: ")))
    alunos.append(notas)

print("\nMédias dos alunos:")
for i in range(3):
    media = sum(alunos[i]) / 3
    print(f"Aluno {i+1}: {alunos[i]} → Média = {media:.1f}")
    
"""
5. Preencha uma matriz 8x8 de forma que ela se assemelhe a um
tabuleiro de xadrez, alternando os valores entre 'B' e 'W' (preto e
branco).
"""

tabuleiro = []
for i in range(8):
    linha = []
    for j in range(8):
        if (i + j) % 2 == 0:
            linha.append('B')  
        else:
            linha.append('W')  
    tabuleiro.append(linha)

print("\nTabuleiro de xadrez 8x8:")
for linha in tabuleiro:
    print(' '.join(linha))
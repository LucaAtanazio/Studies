"""
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida.
"""
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        if j <= i:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
    
for linha in matriz:
    print(linha)
    
# 1 0 0 0 0
# 1 1 0 0 0
# 1 1 1 0 0
# 1 1 1 1 0
# 1 1 1 1 1
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
"""

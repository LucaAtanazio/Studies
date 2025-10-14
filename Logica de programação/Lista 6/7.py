"""
7. Implemente um programa que leia uma matriz 5 x 10 que se refere as respostas de
10 questões de múltipla escolha, referentes a 5 alunos. Leia também um vetor de
10 posições contendo o gabarito de respostas que podem ser A, B, C, D ou E. Seu
programa deverá comparar as respostas de cada candidato com o gabarito e emitir
um vetor denominado resultado, contendo a pontuação correspondente a cada
aluno.
"""

matriz = []
for i in range(5):
    linha = []
    for j in range(10):
        resposta = input(f"Resposta do aluno {i+1}, questão {j+1}: ").upper()
        linha.append(resposta)
    matriz.append(linha)

gabarito = []
for i in range(10):
    g = input(f"Gabarito da questão {i+1}: ").upper()
    gabarito.append(g)

resultado = [0, 0, 0, 0, 0]

for i in range(5):
    for j in range(10):
        if matriz[i][j] == gabarito[j]:
            resultado[i] += 1

for i in range(5):
    print(f"Aluno {i+1} acertou {resultado[i]} questões")

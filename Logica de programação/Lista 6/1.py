"""
1. Implemente um programa que calcule e retorne a soma dos elementos de uma
matriz 5 x 5 de números inteiros.
"""

matriz = []
soma = 0

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

print("Soma dos elementos da matriz:", soma)

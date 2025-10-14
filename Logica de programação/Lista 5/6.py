"""
6. Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os
valores lidos na ordem inversa. Utilizar laço de repetição e vetor(lista).
"""

vetor = [int(input(f"{i+1}° numero: ")) for i in range(6)]
print("\nUltimo ao primiro valor: ")
for num in vetor[::-1]:
    print(num)

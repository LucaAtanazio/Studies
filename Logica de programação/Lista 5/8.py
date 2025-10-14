"""
8. Implemente um programa que leia dois conjuntos de números reais, armazenando-
os em vetor(lista)es.
Após, calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. 
Ao final, imprimir os dois conjuntos e o produto escalar, 
sendo que o produto escalar é dado por: x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn.
"""
list_X = [int(input(f"Lista X -> {i+1}° numero: ")) for i in range(5)]
list_Y = [int(input(f"Lista Y -> {i+1}° numero: ")) for i in range(5)]

produto = 0
for i in range(5):
    produto += list_X[i] * list_Y[i]

print("\n",list_X)
print(list_Y)
print("Produto escalar: ", produto)


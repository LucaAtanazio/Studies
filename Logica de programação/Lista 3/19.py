# 19) Criar um algoritmo que leia dois números e imprimir o quadrado do menor número e
#raiz quadrada do maior número, se for possível.
n1 = int(input("Digite o 1° numero: "))
n2 = int(input("Digite o 2° numero: "))

import math
if n1 > n2:
    print(f"{n1} > {n2}\n{math.sqrt(n1)} e {n2**2} ")
else:
    print(print(f"{n2} > {n1}\n{math.sqrt(n2)} e {n1**2} "))
    
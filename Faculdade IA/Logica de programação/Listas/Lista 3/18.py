# 18) Construir um algoritmo que leia um número e imprima se ele é igual a 5, a 200, a
#400, se está no intervalo entre 500 e 1000, inclusive, ou se ela está fora dos escopos
#anteriores.
n = int(input("Digite um numero: "))

if n == 5:
    print(n)
elif n == 200:
    print(n)
elif n == 400:
    print(n)
elif n > 500 and n < 1000:
    print(f"{n} no intervalo 500--1000")
else:
    print(f"{n} fora dos escopos")
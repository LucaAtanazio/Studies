# 10) Construa um algoritmo que imprima qual o menor e qual o maior valor de dois
#números A e B, lidos através do teclado.
a = int(input("A = "))
b = int(input("B = "))

if a > b:
    print(f"{a} é o Maior valor -> {a} > {b} ")
else:
    print(f"{b} é o Menor valor -> {a} < {b} ")
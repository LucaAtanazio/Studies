# 13) Construa um algoritmo que dado três valores A, B e C, o algoritmo imprima o maior valor.
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a > b and a > c:
    print(f"{a} é maior que {b} e {c}")
elif b > a and b > c:
    print(f"{b} é maior que {a} e {c}")
else:
    print(f"{c} é maior que {a} e {b}")
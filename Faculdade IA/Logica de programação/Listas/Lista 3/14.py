# 14) Dados três valores A, B e C, construa um algoritmo que imprima os valores de forma
#ascendente (do menor para o maior).
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if c <= b <= a:
    print(f"{c} < {b} < {a}")
elif b <= c <= a:
    print(f"{b} < {c} < {a}")
elif b <= a <= c:
    print(f"{b} < {a} < {c}")
elif a <= b <= c:
    print(f"{a} < {b} < {c}")
elif a <= c <= b:
    print(f"{a} < {c} < {b}")
else:
    print(f"{c} < {a} < {b}")


    

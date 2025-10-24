"""
9. Escreva uma função que calcule o n-ésimo termo de uma Progressão
    geométrica, dado o primeiro termo e a razão.
        An = A1 * r**n-1
            Entrada: a1 = 3, r = 2, n = 5
            Resultado: an = 48
"""
a1 = int(input("A1 = "))
r = int(input("R = "))
n = int(input("N = "))

an = a1 * r**(n-1)

print(f"Entrada: A1 = {a1}, r = {r}, n = {n}")
print(f"Resultado: An = {an}")
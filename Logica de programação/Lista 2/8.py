#  8. Crie uma função que receba o primeiro termo, a razão e o número de termos de
#    uma Progressão aritmética, e retorne o n-ésimo termo.
#        An = A1 + (n-1) * r
#    Entrada: a1 = 2, r = 5, n = 4
#    Resultado: an = 17

a1 = int(input("A1 = "))
r = int(input("R = "))
n = int(input("N = "))
an = a1 + (n - 1) * r

print(f"Entrada: A1 = {a1}, r = {r}, n = {n} ")
print(f"Resultado: An = {an}")
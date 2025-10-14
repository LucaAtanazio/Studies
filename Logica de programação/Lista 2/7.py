#  7. Implemente uma função que resolva a equação de segundo grau (ax2 + bx + c = 0) e retorne as raízes.
#      x1, x2 = [-b +- V{ b² - 4ac }] / 2a
#        Entrada: a = 1, b = -3, c = 2
#        Resultado: x1 = 2, x2 = 1
import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(f"Entrada: a = {a}, b = {b}, c = {c}")
print(f"Resultado: x1 = {x1:.2f}, x2 = {x2:.2f}")

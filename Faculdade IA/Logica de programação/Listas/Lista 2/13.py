"""
13. Implemente uma função que, dado um triângulo com dois lados e o ângulo entre
    eles, calcule o terceiro lado usando a Lei dos Cossenos.
        c² = a² + b² - 2ab * cos(C)
            Entrada: a = 5, b = 7, C = 45o
            Resultado: c = 4.95
"""
import math
a = int(input("a = "))
b = int(input("b = "))
C = int(input("c = "))

c = ((a**2) + (b**2) - (2*a*b) * math.cos(C))**2
 
print(f"Entrada: a = {a}, b = {b}, C = {C}")
print(f"Resultado: c = {c:.2f}")
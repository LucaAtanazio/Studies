"""
10. Desenvolva uma função que calcule o seno de um ângulo (em graus).
    seno(x) = sin(x)
        Entrada: x = 30o
        Resultado: seno(x) ≈ 0.5
"""
import math

x = float(input("x = "))
seno = math.ceil(math.sin(x))

print(f"Entrada: x = {x}")
print(f"Resultado: seno({x}) = {seno}")

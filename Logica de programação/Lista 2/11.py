#   11. Cosseno de um ângulo: Implemente uma função que calcule o cosseno de um
#    ângulo (em graus).
#        cosseno(x) = cos(x)
#    Entrada: x = 60o
#    Resultado: cosseno(x) ≈ 0.5
import math

x = float(input("x = "))
cosseno = math.ceil(math.cos(x))

print(f"Entrada: x = {x}")
print(f"Resultado: cosseno({x}) = {cosseno}")


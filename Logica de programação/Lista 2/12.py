#    12. Tangente de um ângulo: Escreva uma função que calcule a tangente de um
#    ângulo (em graus).
#        tangente(x) = tan(x)
#    Entrada: x = 45o
#    Resultado: tangente(x) ≈ 1
import math

x = float(input("x = "))
tangente = math.ceil(math.tan(x))

print(f"Entrada: x = {x}")
print(f"Resultado: tangente({x}) = {tangente}")

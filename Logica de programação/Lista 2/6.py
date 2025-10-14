#   6. Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer
#       no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles. A fórmula que
#       efetua tal cálculo é:  d = V{ (x2 - x1)² + (y2 - y1)² }
import math

x = [int(input(f"Digite o valor de x{i+1}: ")) for i in range(2)]
y = [int(input(f"Digite o valor de y{i+1}: ")) for i in range(2)]

d =  print(f"{math.sqrt(pow((x[1] - x[0]), 2) + pow((y[1] - y[0]), 2)):.2f}")


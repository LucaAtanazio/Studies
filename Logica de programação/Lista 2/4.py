#   4. Desenvolva um programa que leia um número positivo do usuário e calcule o
#       logaritmo desse número na base 10.
import math
n = int(input("Digite um numero: "))
if n > 0:
    print(f"{math.log10(n):.2f}")
else:
    print("Use apenas numeros positivos")
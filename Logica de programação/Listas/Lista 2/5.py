"""
5. Desenvolva um programa que leia um número positivo do usuário, calcule sua
       raiz quadrada e, em seguida, eleve o resultado ao quadrado (Obs: o resultado
       deve retornar o número original).
"""
import math
n = int(input("Digite um numero positvo: "))
if n < 0:
    print("Use apenas numeros positivos")
else:
    res = pow(math.sqrt(n), 2)
    print(f"{res:.2f}")
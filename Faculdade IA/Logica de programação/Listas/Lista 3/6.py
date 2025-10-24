# 6) Escreva um algoritmo que leia um número e 
# caso ele seja positivo ou igual a zero imprima a raiz quadrada do número
#e caso ele seja negativo o quadrado do número.
import math
n = int(input("Digite um numero: "))
if n >= 0:
    print(math.sqrt(n))
else:
    print(n**2)
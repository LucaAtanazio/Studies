# 4) Escreva um algoritmo para determinar se um dado número N (recebido através
#do teclado) é POSITIVO, NEGATIVO ou NULO.
n = int(input("Digite um numero: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Nulo")
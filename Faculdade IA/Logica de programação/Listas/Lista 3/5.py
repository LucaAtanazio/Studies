# 5) Construir um algoritmo que leia dois números e efetue a adição. 
# Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
#caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
n1 = int(input("Digite o 1° numero: "))
n2 = int(input("Digite o 2° numero: "))

if (n1 + n2) > 20:
    print((n1 + n2) + 8)
else:
    print((n1 + n2) - 5)
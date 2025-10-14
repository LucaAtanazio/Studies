# 9) Escreva um algoritmo para determinar 
# se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário.
a = int(input("A = "))
b = int(input("B = "))
if a % b == 0:
    print(f"{a} é divisivel por {b}")
else:
    print(f"Não, {a} não é divisivel por {b}")
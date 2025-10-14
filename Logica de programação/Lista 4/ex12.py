menor = float('inf')
maior = float('-inf')

for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f"Maior: {maior}, Menor: {menor}")
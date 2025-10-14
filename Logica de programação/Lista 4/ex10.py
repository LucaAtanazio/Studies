soma = 0
print("Números de 1 a 100 e média:")
for i in range(1, 101):
    print(i, end=' ')
    soma += i
print(f"\nMédia: {soma/100}")
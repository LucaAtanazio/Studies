inicio = int(input("Limite inferior: "))
fim = int(input("Limite superior: "))
soma = 0

print(f"Pares entre {inicio} e {fim}:")
for i in range(inicio + 1, fim):
    if i % 2 == 0:
        print(i, end=' ')
        soma += i

print(f"\nSomatório: {soma}")
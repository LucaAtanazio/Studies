n = int(input("Digite N: "))
print(f"Divisores de {n}:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
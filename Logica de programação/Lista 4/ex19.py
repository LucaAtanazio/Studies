t1 = int(input("1º termo: "))
t2 = int(input("2º termo: "))
n = int(input("Quantos termos? "))
soma = t1 + t2

print("Série de Ricci:", t1, t2, end=' ')

for _ in range(n-2):
    proximo = t1 + t2
    print(proximo, end=' ')
    soma += proximo
    t1, t2 = t2, proximo

print(f"\nSoma dos termos: {soma}")
n = int(input("Digite o valor de N: "))
s = 0.0

for i in range(1, n+1):
    s += 1/(i**i)

print(f"S = {s:.4f}")
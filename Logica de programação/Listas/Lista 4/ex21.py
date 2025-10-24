n = int(input("Digite o valor de N: "))
h = 0
sinal = 1

for i in range(1, n+1):
    print(f"{1}/{i}")
    h += sinal * (1/i)
    sinal *= -1  # Alterna o sinal

print(f"H = {h:.2f}")
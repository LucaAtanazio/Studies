n = int(input("Digite o valor de N: "))
h = 0

for i in range(1, n+1):
    print(f"{1}/{i}")
    h += 1/i

print(f"H = {h:.2f}")
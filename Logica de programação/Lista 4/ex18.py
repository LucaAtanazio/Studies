n = int(input("Digite N: "))
a, b = 1, 1
print("Série de Fibonacci: ")
for _ in range(n):
    print(a, end='  ')
    a, b = b, a + b
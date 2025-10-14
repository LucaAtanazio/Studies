a = int(input("Digite A: "))
b = int(input("Digite B: "))

original_a = a
original_b = b

# Máximo Divisor Comum
while b:
    a, b = b, a % b


if a == 1:
    print(f"{original_a} e {original_b} são primos entre si")
else:
    print(f"{original_a} e {original_b} NÃO são primos entre si")  

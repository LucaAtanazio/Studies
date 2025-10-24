n = int(input("Digite N: "))
fatorial = 1
if n < 0:
    print("Não use numero negativos, apenas positivos")
    
else:
    for i in range(1, n+1):
        fatorial *= i

    print(f"{n}! = {fatorial}")
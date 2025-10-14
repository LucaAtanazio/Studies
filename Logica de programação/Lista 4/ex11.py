num = int(input("Quantos números? "))
maior = 0
menor = 999999


for i in range(0,  num + 1):
    n = int(input(f"Digite o {i+1}º número: "))
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f"""
      Maior: {maior}
      Menor: {menor}
      """)
"""
3. Faça um programa que receba do usuário um vetor(lista) com 20 posições. Em
seguida deverá ser impresso o maior e o menor elemento do vetor(lista).
"""

SSS = [float(input(f"Numero {i+1}°: ")) for i in range(20)] 
print(SSS)

maior, menor = max(SSS), min(SSS)

print("Maior numero: ", maior)
print("Menor numero: ", menor)


"""
4. Fazer um programa para ler 15 valores e, em seguida, mostrar o valor e a posição
onde se encontram o maior e o menor valor.
"""

S = [float(input(f"Numero {i+1}°: ")) for i in range(15)] 
print(S)

maior, menor = max(S), min(S)
pos_max, pos_min = S.index(maior), S.index(menor)

print("Maior numero: ", pos_max +1, "°: ", maior)
print("Menor numero: ", pos_min +1, "°: ", menor)

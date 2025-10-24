votos = {'A': 0, 'B': 0, 'C': 0, 'Branco': 0, 'Nulo': 0}

print("Opções: 1-A, 2-B, 3-C, 4-Branco, 5-Nulo")
for i in range(20):
    while True:
        voto = input(f"Eleitor {i+1}: ")
        if voto in ['1', '2', '3', '4', '5']:
            break
        print("Inválido! Digite 1-5")
    
    if voto == '1': votos['A'] += 1
    elif voto == '2': votos['B'] += 1
    elif voto == '3': votos['C'] += 1
    elif voto == '4': votos['Branco'] += 1
    else: votos['Nulo'] += 1

print("\nResultado:")
print(f"A: {votos['A']}, B: {votos['B']}, C: {votos['C']}")
print(f"Brancos: {votos['Branco']}, Nulos: {votos['Nulo']}")

max_votos = max(votos['A'], votos['B'], votos['C'])
vencedores = []
if votos['A'] == max_votos: vencedores.append('A')
if votos['B'] == max_votos: vencedores.append('B')
if votos['C'] == max_votos: vencedores.append('C')

if len(vencedores) > 1:
    print(f"Empate entre: {', '.join(vencedores)}")
else:
    print(f"Vencedor: {vencedores[0]}")
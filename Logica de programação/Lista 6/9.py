"""
9. Criar um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de
uma loja, em que cada linha represente um mês do ano, e cada coluna, uma semana
do mês. Para fins de simplificação considere que cada mês possui somente 4
semanas. Calcule e imprima: - Total vendido em cada mês do ano; - Total vendido
em cada semana durante todo o ano; - Total vendido no ano.
"""

matriz = []

for i in range(12):
    linha = []
    for j in range(4):
        valor = float(input(f"Vendas do mês {i+1}, semana {j+1}: "))
        linha.append(valor)
    matriz.append(linha)

total_mes = []
for i in range(12):
    soma = 0
    for j in range(4):
        soma += matriz[i][j]
    total_mes.append(soma)

total_semana = [0, 0, 0, 0]
for j in range(4):
    for i in range(12):
        total_semana[j] += matriz[i][j]

total_ano = 0
for valor in total_mes:
    total_ano += valor

print(f"""
- Total vendido em cada mês do ano: {total_mes}
\n- Total vendido em cada semana durante todo o ano: {total_semana}
\n- Total vendido no ano: {total_ano}
""")

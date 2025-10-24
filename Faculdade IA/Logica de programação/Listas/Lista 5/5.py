"""
5. Faça um programa para ler a nota da prova de 15 alunos e armazene num
vetor(lista), calcule e imprima a média geral.
"""
sala = [float(input(f"Nota {i+1}: ")) for i in range(15)]

media = sum(sala) / len(sala)
print(f"Media da sala de aula: {media:.2f}")

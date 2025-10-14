#4. Faça um programa que receba duas notas, calcule e mostre a média ponderada 
#   dessas notas, considerando peso 7 para a primeira e peso 3 para a segunda

nota1 = float(input("Digite a sua 1° nota: "))
nota1 = nota1 * 7

nota2 = float(input("Digite a sua 2° nota: "))
nota2 = nota2 * 3

media_pond = (nota1 + nota2) / 7 + 3 

print(f"""
Calculo com peso 1 e 2:
nota 1: {nota1:.1f} 
nota 2: {nota2:.1f} 
Media ponderada: {media_pond:.1f}
""")
"""
Questão 20
Construa um algoritmo para determinar se o indivíduo está com um peso favorável. 
Essa situação é determinada através do IMC (Índice de Massa Corpórea),que é definida como:

imc = peso / altura**2

IMC abaixo de 20	Abaixo do peso
IMC de 20 até 25	Peso Normal
IMC de 25 até 30	Sobrepeso
IMC de 30 até 40	Obeso
IMC de 40 e acima	Obeso Mórbido
"""
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura(m): "))

imc = peso / altura**2

if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc < 25:
    print("Peso Normal")
elif imc > 25 and imc < 30:
    print("Sobrepeso")
elif imc > 30 and imc < 40:
    print("Obeso")
elif imc >= 40:
    print("Obeso Mórbido")

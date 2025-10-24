# 16) Escreva um algoritmo que leia um número e informe se ele é divisível por 10, 
# por 5 ou por 2 ou se não é divisível por nenhum deles.
n = int(input("Digite um numero: "))

if n % 10 == 0:
    print("Divisivel por 10"
        "\nDivisivel por 5"
        "\nDivisivel por 2")
elif n % 5 == 0:
    print("Divisivel por 5")
elif n % 2 == 0:
    print("Divisivel por 2")
else:
    print("Não é divisivel com as opções")
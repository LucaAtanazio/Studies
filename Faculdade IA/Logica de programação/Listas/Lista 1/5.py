# 5. Crie um programa que leia dois números inteiros e imprima o dividendo, divisor, quociente e resto.
dividendo = int(input("Digite um numero inteiro: "))
divisor = int(input("Digite outro numero inteiro: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"""
      Dividendo: {dividendo}
      Divisor: {divisor}
      Quociente: {quociente}
      Resto: {resto}
      """)

numero = int(input("Digite um numero: "))
if numero < 0:
  print("Digite apenas numeros positivos")
else:
  fatorial = 1
  for i in range(1, numero + 1):
    fatorial = fatorial * i
  print(fatorial)
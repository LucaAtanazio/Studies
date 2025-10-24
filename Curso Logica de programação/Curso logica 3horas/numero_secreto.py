import random
valor_aleatorio = random.randint(1, 10)
chute = int(input("Digite seu chute: "))
if chute < valor_aleatorio:
  print("Maior")
elif chute > valor_aleatorio:
  print("Menor")
while chute != valor_aleatorio:
   chute = int(input("Tente de novo: "))
   if chute < valor_aleatorio:
     print("Maior")
   elif chute > valor_aleatorio:
     print("Menor")
else:
  print("Acertou")

  
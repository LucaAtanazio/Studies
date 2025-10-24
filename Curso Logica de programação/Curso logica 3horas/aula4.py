#coleções (listas)
#lista
precos = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
#indices   0   1  2    3  4    5  6    7    8    9    10  11     
print(precos [7])
print(precos.index(140)) 

#Coleção de dados de diversos tipos
diver = [32, "mascaco", False]
for item in diver:
  print(item)

#Laços em repetição
for precos in precos:
  print(precos)

for i in range(0, 101, 10):
  print(i)

espaco = "          "
print(espaco)

# some os valores dados na colação "Idades [15, 46, 75, 34, 23]" e imprima o resultado"
soma = 0
idades = [15, 46, 75, 34, 23]
for i in idades:
  soma = soma + i  
  print(soma)

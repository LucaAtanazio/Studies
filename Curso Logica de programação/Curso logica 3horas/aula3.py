#laços de repetição + listas

for palavra in range(1,4):
  print("carregando...")

for item in range(1,70):
  print(item)
for item in range(1, 81, 4):
  print(item)

jojo = ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne", "Johnny", "Josuke"]
for nome in jojo:
  print(nome)

''' 
input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
  print valor_inicial
'''
valor_maximo = int(input("Digite seu valor maximo: "))
valor_inicial = 1 
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)

espaco = "          "
#condicionais
# if, elif, else
print("1° Questão:")
print(espaco)
#trabalho terminado?
trabalho_terminado = input("Terminou seu trabalho? (sim/não) :    ")
if trabalho_terminado == "sim":
  print("Bora toma uma")

else:
  print("Não vai naummmmm")

print(espaco)
print(espaco)

print("2° Questão:")
print(espaco)
#Mano, me ajuda aqui a empurrar o sofá aqui em casa
#Sim == "Blz, vou te ajudar"
#Não == "Agora não posso, chama nosso irmão"
empurrar_sofa = input(" - Mano, me ajuda aqui a empurrar o sofá aqui em casa? (sim/não) :  ")
if empurrar_sofa == "sim":
  print(" - Blz, vou te ajudar")
else:
  print(" - Agora não posso, chama nosso irmão")

print(espaco)
print(espaco)

print("3° Questão:")
print(espaco)
#Eu cheguei atrasado na aula, ainda posso entrar?
#Se essa for a sua primeira vez chegando atrasado, você pode entrar, caso contrário, irá tomar uma suspensão
numero_de_atracos = int(input("Numero de atrasos do aluno: "))
if numero_de_atracos <= 2:
  print("Você pode entrar")
else:
  print("Pois tome suspensão na boca pra dexa de ser leso")

print(espaco)
print(espaco)

print("4° Questão:")
print(espaco)
#Escreva um programa que retorne o maior valor entre dois números
'''  
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print primeiro valor é maior
else 
  print segundo valor é maior
'''
primeiro_valor = int(input("1° = "))
segundo_valor = int(input("2° = "))
if primeiro_valor > segundo_valor:
  print("primeiro valor é maior")
else:
  print("segundo valor é maior")

print(espaco)
print(espaco)

print("5° Questão:")
print(espaco)
# Calcular a média de duas notas de um aluno e dizer se ele foi aprovado ou reprovado
print("Calculo da média de um aluno")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))  
media = round((nota1 + nota2)/ 2, 2) 
print(media)

if media >= 70:
  print("Aluno aprovado")
elif media < 70 and media >= 50:
  print("Recuperação")

else:
  print("Aluno reprovado")
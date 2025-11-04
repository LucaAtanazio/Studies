#variaveis

#numeros
velocidade_internet = 10
print("A velocidade da minha internet é ", velocidade_internet)
nota =  8.5 # float = numeros decimais
print("Minha nota é ", nota)

#valores booleanos
esta_aberto = True
print("Cinema esta aberto = ", esta_aberto)

# Strings
nome_curso = "Matemática"
print("Nome do curso = ", nome_curso)

# PROBLEMA 1 - Escreva um programa que retorne o valor hora de um funcionario com base no seu salario mensal e horas trabalhadas por mês
valor_hora = 0 
salario_mensal = float(input("Digite seu salario mensal: R$"))
horas_trabalhadas_por_mes = input("Digite suas horas trabalhadas por mês: "))
valor_hora = round(salario_mensal/horas_trabalhadas_por_mes, 2)
print("Calculo do valor hora: ")
print("Salario mensal: R$", salario_mensal)
print("Horas trabalhadas por mês: ", horas_trabalhadas_por_mes)
print("Valor hora: R$", valor_hora)

# 12) A prefeitura de uma cidade abriu uma linha de crédito para os funcionários estatutários.
# O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. 
# Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação, 
# e informar se o empréstimo pode ou não ser concedido.
sal_br = float(input("Valor do salario bruto: "))
prest = int(input("Valor da prestação: "))
if prest > (sal_br * 0.3):
    print("Seu emprestimos não pode ser concedido")
else:
    print("Seu emprestimos pode ser concedido")

# saudação nome e sobrenome
def saudacao(nome, sobrenome):
    return f"Olá {nome} {sobrenome}, bem vindo"
print(saudacao("Luca", "Atanazio"))
print(saudacao("Maryana", "Evangelista"))

# criar perfil
def criar_perfil(nome, e_mail, senha):
    return f"""
Nome: {nome}
E-mail: {e_mail}
Senha: {senha}
"""
print(criar_perfil(nome="Luca", e_mail="atanazio12@", senha=1295))

# soma de todos os valores
def soma_total(*numeros):
    total =  0
    for num in numeros:
        total += num
    return total
print(soma_total(40, 60, 25))

# calcular a area do circulo
def calcular_area_circulo(raio):
    pi = 3.14
    area = pi * (raio**2)
    print(f"Área = {area}")
    return area
calcular_area_circulo(25)

soma = lambda x, y :(x + y)*(x*(y)-y)
print(soma(2,9))

# diagonal 
matriz 
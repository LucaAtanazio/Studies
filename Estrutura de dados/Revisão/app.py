# array

lista = [3, 54, 93, 101, 390]
print(lista[1])

# lista encadeada

class No: 
    def __init__(self, item):
        self.item = item  
        self.proximo = None 

no1 = No("Leite")
no2 = No("Ovos")
no3 = No("Pão")

no1.proximo = no2  
no2.proximo = no3  
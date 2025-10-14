"""
10. Faça um programa para ler 10 números DIFERENTES a serem armazenados em
um vetor(lista). 
Os dados deverão ser armazenados no vetor(lista) na ordem que
forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado
anteriormente, o programa deverá pedir para ele digitar outro número. Note que
cada valor digitado pelo usuário deve ser pesquisado no vetor(lista), verificando
se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor(lista)
final que foi digitado, ou seja, sem nenhuma repetição.
"""
print("Faça uma lista sem repetir numeros: ")
  
lista = []  
while len(lista) < 10:  
    num = int(input(f"Digite o {len(lista) + 1}º número: "))
    
    if num in lista:  
        print("Erro: Número repetido! Digite outro valor")
    else:
        lista = lista + [num]  

print("\nLista final sem repetições:", lista)
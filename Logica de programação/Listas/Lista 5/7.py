"""
7. Faça um programa que leia um vetor(lista) de 5 posições para números reais e,
depois, um código inteiro. 
Se o código lido for zero, finalize o programa; 
se for 1,mostre o vetor(lista) na ordem direta; 
se for 2, mostre o vetor(lista) na ordem inversa. 
Caso o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido.
"""

listaaaa = [int(input(f"{i+1}° numero: ")) for i in range(5)]

codigo = int(input("""
    Escolha seu comando:
        0 = End              
        1 = Lista      
        2 = Lista invertida    
    Digite sua opção:               
    """))

if codigo == 0:
    print("Fim do programa")
elif codigo == 1:
    print(listaaaa)
elif codigo == 2:
    for num in listaaaa[::-1]:
        print(num)
else:
    print("Erro! Escolha apenas opções disponiveis")
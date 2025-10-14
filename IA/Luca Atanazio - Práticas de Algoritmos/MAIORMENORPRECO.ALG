Algoritmo "MaiorMenorPreco"

Var
   preco, maior, menor: real
    i: inteiro
    
Inicio
escreva("Digite o preço do 1º produto: ")
    leia(preco)
    maior <- preco
    menor <- preco
    para i de 2 ate 8 faca
        escreva("Digite o preço do ", i, "º produto: ")
        leia(preco)
        se preco > maior entao
            maior <- preco
        fimse
        se preco < menor entao
            menor <- preco
        fimse
    fimpara
    escreva("Maior preço: ", maior)
    escreva("Menor preço: ", menor)
    
Fimalgoritmo

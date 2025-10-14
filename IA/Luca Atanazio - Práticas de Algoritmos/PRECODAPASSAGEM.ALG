Algoritmo "PrecoDaPassagem"

Var
   distancia, preco: real
Inicio
escreva("Digite a distância da viagem (km): ")
    leia(distancia)
    se distancia <= 200 entao
        preco <- distancia * 0.50
    senao
        preco <- distancia * 0.45
    fimse
    escreva("Preço da passagem: R$", preco)

Fimalgoritmo



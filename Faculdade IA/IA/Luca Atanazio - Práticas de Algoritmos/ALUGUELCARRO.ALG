Algoritmo "AluguelCarro"

Var
    carro: caractere
    dias, km: inteiro
    total, valorDiaria, taxaKm: real
    
Inicio
    escreva("Tipo de carro (P-popular/L-luxo): ")
    leia(carro)
    escreva("Dias de aluguel: ")
    leia(dias)
    escreva("Km percorridos: ")
    leia(km)

    se (carro = "P") ou (carro = "p") entao
        valorDiaria <- 90
        se km <= 100 entao
            taxaKm <- 0.20
        senao
            taxaKm <- 0.10
        fimse
    senao se (carro = "L") ou (carro = "l") entao
        valorDiaria <- 150
        se km <= 200 entao
            taxaKm <- 0.30
        senao
            taxaKm <- 0.25
        fimse
    senao
        escreva("Tipo de carro inválido!")
        interrompa
    fimse

    total <- (dias * valorDiaria) + (km * taxaKm)
    escreval("Total a pagar: R$", total:5:2)
Fimalgoritmo
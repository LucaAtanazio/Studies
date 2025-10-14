Algoritmo "MultaDeVelocidade"

Var
    velocidade, excesso, multa: real
    
Inicio
   escreva("Digite a velocidade do carro: ")
    leia(velocidade)
    se velocidade > 80 entao
        excesso <- velocidade - 80
        multa <- 200 + (excesso * 5)
        escreva("Multado! Valor da multa: R$", multa)
    senao
        escreva("Velocidade dentro do limite.")
    fimse
    
Fimalgoritmo

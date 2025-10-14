algoritmo "ClassificaClima"

var
    temperatura: real

inicio
    escreva("Digite a temperatura atual (em °C): ")
    leia(temperatura)

    se temperatura >= 30 então
        escreva("Está muito quente!")
    senão se temperatura >= 20 então
        escreva("O clima está agradável.")
    senão
        escreva("Está frio!")
    fimse

fimalgoritmo
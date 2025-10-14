algoritmo "CalculadoraDescontos"

var
    valorCompra, valorFinal: real

inicio
    escreva("Digite o valor da compra: R$ ")
    leia(valorCompra)

    se valorCompra >= 100 então
        valorFinal <- valorCompra * 0.90
        escreva("Valor com 10% de desconto: R$ ", valorFinal:6:2)
    senão
        valorFinal <- valorCompra
        escreva("Valor sem desconto: R$ ", valorFinal:6:2)
    fimse

fimalgoritmo
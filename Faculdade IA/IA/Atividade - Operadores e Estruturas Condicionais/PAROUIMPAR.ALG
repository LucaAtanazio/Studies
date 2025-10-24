algoritmo "ParOuImpar"
var
    numero: inteiro
    
inicio
    escreva("Digite um número inteiro: ")
    leia(numero)

    se numero % 2 = 0 então
        escreva("O número ", numero, " é PAR")
    senão
        escreva("O número ", numero, " é ÍMPAR")
    fimse
    
fimalgoritmo
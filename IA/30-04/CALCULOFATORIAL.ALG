Algoritmo "CalculoFatorial"

Var
    numero, resultado: inteiro

funcao fatorial(n: inteiro): inteiro
var
    i, fat: inteiro
inicio
    fat <- 1
    para i de 1 ate n faca
        fat <- fat * i
    fimpara
    retorne fat
fimfuncao

Inicio

    escreva("Digite um número para calcular seu fatorial: ")
    leia(numero)

    resultado <- fatorial(numero)
    escreval("O fatorial de ", numero, " é ", resultado)

Fimalgoritmo

Algoritmo "VerificaNPrimo"

Var
    num: inteiro
    primo: logico

funcao ehPrimo(n: inteiro): logico
var
    i: inteiro
inicio
    se n <= 1 entao
        retorne falso
    fimse

    para i de 2 ate n-1 faca
        se n % i = 0 entao
            retorne falso
        fimse
    fimpara
    retorne verdadeiro
fimfuncao

Inicio

    escreva("Digite um número inteiro para verificar se é primo: ")
    leia(num)

    primo <- ehPrimo(num)

    se primo entao
        escreval(num, " é um número primo.")
    senao
        escreval(num, " não é um número primo.")
    fimse
Fimalgoritmo

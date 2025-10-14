Algoritmo "MediaMatriz"

Var
    matriz: vetor[1..3, 1..3] de inteiro
    i, j, soma, totalElementos: inteiro
    media: real
Inicio

    para i de 1 ate 3 faca
        para j de 1 ate 3 faca
            escreva("Digite o valor para a posição [", i, ",", j, "]: ")
            leia(matriz[i, j])
        fimpara
    fimpara

    soma <- 0
    totalElementos <- 3 * 3

    para i de 1 ate 3 faca
        para j de 1 ate 3 faca
            soma <- soma + matriz[i, j]
        fimpara
    fimpara

    media <- soma / totalElementos

    escreval("A média da matriz é: ", media)
Fimalgoritmo


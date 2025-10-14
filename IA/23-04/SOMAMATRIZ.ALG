Algoritmo "SomaMatriz"

Var
    matriz: vetor[1..2, 1..3] de inteiro
    i, j, soma: inteiro
    
Inicio
    para i de 1 ate 2 faca
        para j de 1 ate 3 faca
            escreva("Digite o valor para a posição [", i, ",", j, "]: ")
            leia(matriz[i, j])
        fimpara
    fimpara

    soma <- 0
    para i de 1 ate 2 faca
        para j de 1 ate 3 faca
            soma <- soma + matriz[i, j]
        fimpara
    fimpara

    escreval("A soma da matriz é: ", soma)

Fimalgoritmo

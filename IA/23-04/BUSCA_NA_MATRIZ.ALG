Algoritmo "Busca_na_Matriz"

Var
    matriz: vetor[1..3, 1..3] de inteiro
    i, j, valor: inteiro
    encontrado: logico

Inicio
    para i de 1 ate 3 faca
        para j de 1 ate 3 faca
            escreva("Digite o valor da posição [", i, ",", j, "]: ")
            leia(matriz[i, j])
        fimpara
    fimpara

    escreva("Busca: ")
    leia(valor)

    encontrado <- falso
    para i de 1 ate 3 faca
        para j de 1 ate 3 faca
            se matriz[i, j] = valor entao
                escreval("Valor em [", i, ",", j, "]")
                encontrado <- verdadeiro
            fimse
        fimpara
    fimpara

    se nao encontrado entao
        escreval("O valor ", valor, " não existe.")
    fimse
Fimalgoritmo

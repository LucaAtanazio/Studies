algoritmo "Soma de seus elementos"
var
   matriz: vetor[1..2, 1..3] de inteiro
   soma, i, j: inteiro
inicio
      soma <- 0
      para i de 1 ate 2 faca
           para j de 1 ate 3 faca
                escreva("Digite o valor para [", i, ",", j, "]: ")
                leia(matriz[i,j])
                soma <- soma + matriz[i,j]
           fimpara
      fimpara

      escreval("")
      escreva("Matriz inserida: ")
      para i de 1 ate 2 faca
           para j de 1 ate 3 faca
                escreva(matriz[i,j], " ")
           fimpara
           escreval("")
      fimpara

      escreval("")
      escreva("A soma total dos valores é ", soma)
fimalgoritmo
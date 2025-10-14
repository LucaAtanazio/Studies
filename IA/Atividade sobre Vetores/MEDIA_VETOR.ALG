Algoritmo "Media_Vetor"

Var
   numeros: vetor[1..5] de inteiro
   i, soma: inteiro
   media: real

Inicio
   para i de 1 ate 5 faca
      escreva("Digite o ", i, "º número inteiro: ")
      leia(numeros[i])
   fimpara

   soma <- 0
   para i de 1 ate 5 faca
      soma <- soma + numeros[i]
   fimpara

   media <- soma / 5

   escreval("A média dos números é: ", media:0:2)
Fimalgoritmo

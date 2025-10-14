algoritmo "ParImparPositivoNegativo"

var
   numero: inteiro

inicio
   escreva("Digite um número inteiro: ")
   leia(numero)

   se numero % 2 = 0 entao
      escreva("O número é par")
   senao
      escreva("O número é ímpar")
   fimse

   se numero > 0 entao
      escreva(" e positivo")
   senao
      se numero < 0 entao
         escreva(" e negativo")
      senao
         escreva(" e zero")
      fimse
   fimse

fimalgoritmo
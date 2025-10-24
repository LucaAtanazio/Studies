algoritmo "VerificaMultiplos"

var
   a, b: inteiro

inicio
   escreva("Digite dois números inteiros (separados por espaço): ")
   leia(a, b)

   se (a % b = 0) ou (b % a = 0) entao
      escreva("São múltiplos")
   senao
      escreva("Não são múltiplos")
   fimse

fimalgoritmo
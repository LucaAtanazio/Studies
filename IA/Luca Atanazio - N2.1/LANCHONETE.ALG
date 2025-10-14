algoritmo "Lanchonete"

var
   codigo, quantidade: inteiro
   valor_total: real

inicio
   escreval(" Lanches          Código   Preço")
   escreval("Cachorro Quente    100     R$ 1,20")
   escreval("Bauru simples      101     R$ 1,30")
   escreval("Bauru com ovo      102     R$ 1,50")
   escreval("Hambúrger          103     R$ 1,20")
   escreval("Cheeseburguer      104     R$ 1,30")
   escreval("Refrigerante       105     R$ 1,00")
   
   escreva("Digite o código do item e a quantidade (separados por espaço): ")
   leia(codigo, quantidade)

   escolha codigo
      caso 100
         valor_total <- quantidade * 1.20
      caso 101
         valor_total <- quantidade * 1.30
      caso 102
         valor_total <- quantidade * 1.50
      caso 103
         valor_total <- quantidade * 1.20
      caso 104
         valor_total <- quantidade * 1.30
      caso 105
         valor_total <- quantidade * 1.00
      outrocaso
         escreva("Código inválido")
         valor_total <- 0
   fimescolha

   se valor_total > 0 entao
      escreva("Valor a pagar: R$", valor_total)
   fimse

fimalgoritmo
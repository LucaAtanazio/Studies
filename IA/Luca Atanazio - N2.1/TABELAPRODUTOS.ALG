algoritmo "TabelaProdutos"

var
   codigo, quantidade: inteiro
   preco_unitario, total: real

inicio
   escreval(" Código do Produto   Preço Unitário    ")
   escreval("     1001             R$ 5,32          ")
   escreval("     1324             R$ 6,45          ")
   escreval("     6548             R$ 2,37          ")
   escreval("     0987             R$ 5,32          ")
   escreval("     7623             R$ 6,45          ")

   escreva("Digite o código do produto e a quantidade: ")
   leia(codigo, quantidade)

   se codigo = 1001 entao
      preco_unitario <- 5.32
   senao
      se codigo = 1324 entao
         preco_unitario <- 6.45
      senao
         se codigo = 6548 entao
            preco_unitario <- 2.37
         senao
            se codigo = 0987 entao
               preco_unitario <- 5.32
            senao
               se codigo = 7623 entao
                  preco_unitario <- 6.45
               senao
                  escreval("Código inválido!")
                  preco_unitario <- 0
               fimse
            fimse
         fimse
      fimse
   fimse
   se preco_unitario > 0 entao
      total <- preco_unitario * quantidade
      escreval("Total a pagar: R$ ", total:5:2)
   fimse

fimalgoritmo
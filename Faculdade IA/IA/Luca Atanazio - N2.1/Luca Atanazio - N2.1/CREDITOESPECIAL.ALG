algoritmo "CreditoEspecial"

var
   saldo_medio, credito: real

inicio
   escreva("Digite o saldo médio do último ano: ")
   leia(saldo_medio)

   se saldo_medio <= 200 entao
      credito <- 0
   senao
      se saldo_medio <= 400 entao
         credito <- saldo_medio * 0.20
      senao
         se saldo_medio <= 600 entao
            credito <- saldo_medio * 0.30
         senao
            credito <- saldo_medio * 0.40
         fimse
      fimse
   fimse

   escreva("Saldo médio: R$", saldo_medio)
   escreval("Crédito disponível: R$", credito)

fimalgoritmo
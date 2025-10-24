algoritmo "CalculoIPI"

var
   ipi: real
   cod1, cod2, quant1, quant2: inteiro
   valor1, valor2, total: real

inicio
   escreva("Digite a porcentagem do IPI: ")
   leia(ipi)
   
   escreva("Digite código, valor unitário e quantidade da peça 1 : ")
   leia(cod1, valor1, quant1)
   escreva("Digite código, valor unitário e quantidade da peça 2 : ")
   leia(cod2, valor2, quant2)

   total <- (valor1*quant1 + valor2*quant2) * (ipi/100 + 1)
   escreva("Valor total a pagar: R$", total)

fimalgoritmo
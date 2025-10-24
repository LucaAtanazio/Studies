algoritmo "PrecoVeiculo"

var
   custo_fabrica, preco_final: real

inicio
   escreva("Digite o custo de fábrica do veículo: ")
   leia(custo_fabrica)

   preco_final <- custo_fabrica * 1.28 * 1.45
   escreva("Preço final ao consumidor: R$", preco_final)

fimalgoritmo
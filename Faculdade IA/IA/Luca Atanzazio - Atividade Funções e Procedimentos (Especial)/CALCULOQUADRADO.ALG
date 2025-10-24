Algoritmo "CalculoQuadrado"
//  
//  

Var
   numero, resultado: real

Funcao CalculoQuadrado(num: real): real
Inicio
      Retorne num * num
FimFuncao

Procedimento lerNumero()
inicio
      escreva("Digite um numero: ")
      leia(numero)
FimProcedimento

Inicio
   LerNumero()
   resultado <- CalculoQuadrado(numero)
   Escreval("O quadrado de ", numero," é: ", resultado)
Fimalgoritmo


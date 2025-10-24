algoritmo "PesoIdeal"

var
   altura: real
   sexo: caractere
   peso_ideal: real

inicio
   escreva("Digite a altura (em metros): ")
   leia(altura)

      escreva("Digite o sexo (M/F): ")
      leia(sexo)


      se sexo = "M" ou sexo = "m" entao
         peso_ideal <- (72.7 * altura) - 58
         escreva("Peso ideal: ", peso_ideal:4:2, " kg")
      senao
         se sexo = "F" ou sexo = "f" entao
            peso_ideal <- (62.1 * altura) - 44.7
            escreva("Peso ideal: ", peso_ideal:4:2, " kg")
         senao
            escreva("Sexo inválido! Digite 'M' ou 'F'.")
         fimse
      fimse
   fimse
fimalgoritmo

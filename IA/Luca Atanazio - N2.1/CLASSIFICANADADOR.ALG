algoritmo "ClassificaNadador"

var
   idade: inteiro

inicio
   escreva("Digite a idade do nadador: ")
   leia(idade)

   escolha idade
      caso 5, 6, 7
         escreva("Infantil A")
      caso 8, 9, 10
         escreva("Infantil B")
      caso 11, 12, 13
         escreva("Juvenil A")
      caso 14, 15, 16, 17
         escreva("Juvenil B")
      outrocaso
         se idade >= 18 entao
            escreva("Adulto")
         senao
            escreva("Idade inválida")
         fimse
   fimescolha

fimalgoritmo
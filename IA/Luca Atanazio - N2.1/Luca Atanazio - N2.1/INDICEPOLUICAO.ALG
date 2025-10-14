algoritmo "IndicePoluicao"

var
   indice: real

inicio
   escreva("Digite o índice de poluição medido: ")
   leia(indice)

   se indice >= 0.05 e indice <= 0.25 entao
      escreva("Índice dentro do aceitável")
   senao
      se indice >= 0.3 e indice < 0.4 entao
         escreva("Notificar indústrias do 1º grupo para suspender atividades")
      senao
         se indice >= 0.4 e indice < 0.5 entao
            escreva("Notificar indústrias do 1º e 2º grupos para suspender atividades")
         senao
            se indice >= 0.5 entao
               escreva("Notificar todas as indústrias para suspender atividades")
            fimse
         fimse
      fimse
   fimse

fimalgoritmo
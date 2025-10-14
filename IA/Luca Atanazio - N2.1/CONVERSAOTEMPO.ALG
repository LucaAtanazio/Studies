algoritmo "ConversaoTempo"

var
   segundos, horas, minutos, seg_restantes: inteiro

inicio
   escreva("Digite o tempo em segundos: ")
   leia(segundos)

   horas <- segundos \ 3600
   seg_restantes <- segundos % 3600
   minutos <- seg_restantes \ 60
   seg_restantes <- seg_restantes % 60

   escreva("Tempo: ", horas, "h ", minutos, "m ", seg_restantes, "s")

fimalgoritmo
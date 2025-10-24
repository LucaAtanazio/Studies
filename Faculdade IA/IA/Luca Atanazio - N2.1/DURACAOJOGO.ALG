algoritmo "DuracaoJogo"

var
   hora_inicio, hora_fim, duracao: inteiro

inicio
   escreva("Digite a hora de início e fim (separadas por espaço): ")
   leia(hora_inicio, hora_fim)

   se hora_fim > hora_inicio entao
      duracao <- hora_fim - hora_inicio
   senao
      duracao <- (24 - hora_inicio) + hora_fim
   fimse

   escreva("Duração do jogo: ", duracao, " horas")

fimalgoritmo
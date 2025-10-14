algoritmo "IdadeEmDias"
var
   anos, meses, dias, total_dias: inteiro

inicio
   escreva("Digite a idade em anos, meses e dias (separados por espaço): ")
   leia(anos, meses, dias)

   total_dias <- anos*365 + meses*30 + dias
   escreva("Idade expressa em dias: ", total_dias)

fimalgoritmo
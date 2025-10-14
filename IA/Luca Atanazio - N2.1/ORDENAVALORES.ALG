algoritmo "OrdenaValores"
var
   i: inteiro
   a, b, c, temp: real
inicio
   escreva("Digite i (1, 2 ou 3) e três valores reais : ")
   leia(i, a, b, c)

   se i = 1 entao
      se a > b entao
         temp <- a
         a <- b
         b <- temp
      fimse
      se b > c entao
         temp <- b
         b <- c
         c <- temp
      fimse
      se a > b entao
         temp <- a
         a <- b
         b <- temp
      fimse
      escreva(a, " ", b, " ", c)
   senao
      se i = 2 entao
         se a < b entao
            temp <- a
            a <- b
            b <- temp
         fimse
         se b < c entao
            temp <- b
            b <- c
            c <- temp
         fimse
         se a < b entao
            temp <- a
            a <- b
            b <- temp
         fimse
         escreva(a, " ", b, " ", c)
      senao
         se i = 3 entao
            se (a > b) e (a > c) entao
               temp <- a
               a <- b
               b <- temp
            senao
               se (c > a) e (c > b) entao
                  temp <- c
                  c <- b
                  b <- temp
               fimse
            fimse
            escreva(a, " ", b, " ", c)
         senao
            escreva("Valor de i inválido")
         fimse
      fimse
   fimse

fimalgoritmo
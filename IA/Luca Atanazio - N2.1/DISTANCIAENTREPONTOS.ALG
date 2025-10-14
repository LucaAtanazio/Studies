algoritmo "DistanciaEntrePontos"
var
   x1, y1, x2, y2, distancia: real
inicio
   escreva("Digite as coordenadas do primeiro ponto (x1 y1): ")
   leia(x1, y1)
   escreva("Digite as coordenadas do segundo ponto (x2 y2): ")
   leia(x2, y2)

   distancia <- raizq((x2-x1)^2 + (y2-y1)^2)
   escreva("A distância entre os pontos é: ", distancia)
fimalgoritmo
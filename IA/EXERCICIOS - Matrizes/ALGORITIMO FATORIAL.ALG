Algoritmo "Algoritimo Fatorial"
//
//
//
//
Var
n: inteiro

funcao fatorial(a: inteiro): inteiro
   Var
   resultado, i: inteiro

   inicio
             resultado
                para i  de a ate 1  passo -1 faca
                  fatorial <- fatorial * i
                fimpara
             retorne resultado
fimfuncao

Inicio
escreval("Informe o numero:")
leia(n)
escreval("O fatorial de ", n, " é: ", fatorial(n))
Fimalgoritmo
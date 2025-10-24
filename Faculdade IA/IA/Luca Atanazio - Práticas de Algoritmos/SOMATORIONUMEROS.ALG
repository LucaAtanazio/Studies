Algoritmo "SomatorioNumeros"

Var
   num, soma: inteiro

Inicio
soma <- 0
    repita
        escreva("Digite um número (1111 para parar): ")
        leia(num)
        se num <> 1111 entao
            soma <- soma + num
        fimse
    ate num = 1111
    escreva("Somatório: ", soma)
    
Fimalgoritmo

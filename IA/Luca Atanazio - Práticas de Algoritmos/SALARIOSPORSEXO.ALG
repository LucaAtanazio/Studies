Algoritmo "SalariosPorSexo"

Var
   salario, totalH, totalM: real
    sexo, continuar: caractere
    contadorH, contadorM: inteiro

Inicio
 totalH <- 0
    totalM <- 0
    contadorH <- 0
    contadorM <- 0

    repita
        escreva("Sexo (M/F): ")
        leia(sexo)
        escreva("Salário: R$ ")
        leia(salario)

        se (sexo = "M") ou (sexo = "m") entao
            totalH <- totalH + salario
            contadorH <- contadorH + 1
        senao se (sexo = "F") ou (sexo = "f") entao
            totalM <- totalM + salario
            contadorM <- contadorM + 1
        senao
            escreval("Sexo inválido! Use M ou F.")
        fimse

        escreva("Continuar? (S/N): ")
        leia(continuar)
    ate (continuar = "N") ou (continuar = "n")
Fimalgoritmo

Algoritmo "CalculoDeIMC"

Var
   peso, altura, imc: real
   classificacao: caractere
Inicio
   escreva("Digite o peso (kg): ")
    leia(peso)
    escreva("Digite a altura (m): ")
    leia(altura)
    
    imc <- peso / (altura ^ 2)
    escreval("")
    
    se imc < 18.5 entao
        classificacao <- "Abaixo do peso"
        escreva(classificacao)
    senao se imc < 25 entao
        classificacao <- "Peso ideal"
        escreva(classificacao)
    senao se imc < 30 entao
        classificacao <- "Sobrepeso"
        escreva(classificacao)
    senao se imc < 40 entao
        classificacao <- "Obesidade"
        escreva(classificacao)
    senao se imc < 50 entao
        classificacao <- "Obesidade mórbida"
        escreva(classificacao)
    senao
        classificacao <- "Obesidade mórbida grave"
        escreva(classificacao)
    fimse
    
    
Fimalgoritmo

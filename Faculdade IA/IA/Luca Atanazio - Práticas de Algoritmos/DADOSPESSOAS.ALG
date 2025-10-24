algoritmo "DadosPessoas"

var
    nome, nomeMaisVelho, nomeMulherJovem, sexo, continuar: caractere
    idade, somaIdades, contHomens30, contMulheres18, contTotal: inteiro
    idadeMaisVelho, idadeMulherJovem: inteiro
    media: real

inicio
    somaIdades <- 0
    contTotal <- 0
    contHomens30 <- 0
    contMulheres18 <- 0
    idadeMaisVelho <- 0
    idadeMulherJovem <- 999

    repita
        escreva("Nome: ")
        leia(nome)
        escreva("Idade: ")
        leia(idade)
        escreva("Sexo (M/F): ")
        leia(sexo)

        somaIdades <- somaIdades + idade
        contTotal <- contTotal + 1

        se idade > idadeMaisVelho entao
            idadeMaisVelho <- idade
            nomeMaisVelho <- nome
        fimse

        se (sexo = "F" ou sexo = "f") e idade < idadeMulherJovem entao
            idadeMulherJovem <- idade
            nomeMulherJovem <- nome
        fimse

        se (sexo = "M" ou sexo = "m") e idade > 30 entao
            contHomens30 <- contHomens30 + 1
        fimse

        se (sexo = "F" ou sexo = "f") e idade < 18 entao
            contMulheres18 <- contMulheres18 + 1
        fimse

        escreva("Continuar? (S/N): ")
        leia(continuar)
    ate continuar = "N" ou continuar = "n"

    media <- somaIdades / contTotal

    escreva("a) Pessoa mais velha: ", nomeMaisVelho)
    se idadeMulherJovem <> 999 entao
        escreva("b) Mulher mais jovem: ", nomeMulherJovem)
    senao
        escreva("b) Nenhuma mulher cadastrada")
    fimse
    escreva("c) Média de idade: ", media:2:2)
    escreva("d) Homens com mais de 30 anos: ", contHomens30)
    escreva("e) Mulheres com menos de 18 anos: ", contMulheres18)
    
fimalgoritmo
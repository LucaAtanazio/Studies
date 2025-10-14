algoritmo "AprovacaoEscolar"

var
    nome: caractere
    nota1, nota2, nota3, media: real

inicio
    escreva("Nome do aluno: ")
    leia(nome)
    escreva("Digite a 1ª nota: ")
    leia(nota1)
    escreva("Digite a 2ª nota: ")
    leia(nota2)
    escreva("Digite a 3ª nota: ")
    leia(nota3)

    media <- (nota1 + nota2 + nota3) / 3

    escreva("Aluno: ", nome, " - Média: ", media:2:1, " - Situação: ")

    se media >= 7 então
        escreva("APROVADO")
    senão
        se media >= 5 então
            escreva("RECUPERAÇÃO")
        senão
            escreva("REPROVADO")
        fimse
    fimse

fimalgoritmo
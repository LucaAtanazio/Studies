Algoritmo "ExibindoMensagens"

Var
    nome: vetor[1..3] de caractere
    idade: vetor[1..3] de inteiro
    i: inteiro

procedimento exibirMensagem(nomePessoa: caractere; idadePessoa: inteiro)

inicio
    escreval("Olá ", nomePessoa, "! Você tem ", idadePessoa, " anos.")
fimprocedimento

Inicio
    para i de 1 ate 3 faca
        escreva("Digite o nome da pessoa ", i, ": ")
        leia(nome[i])
        escreva("Digite a idade de ", nome[i], ": ")
        leia(idade[i])
    fimpara

    escreval("\nMensagens:")
    para i de 1 ate 3 faca
        exibirMensagem(nome[i], idade[i])
    fimpara
Fimalgoritmo

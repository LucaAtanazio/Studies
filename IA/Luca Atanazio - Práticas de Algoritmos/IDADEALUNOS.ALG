algoritmo "IdadeAlunos"

var
    idade, soma, cont: inteiro
    media: real
    
inicio
    soma <- 0
    cont <- 0
    repita
        escreva("Idade do aluno (999 para parar): ")
        leia(idade)
        se idade <> 999 entao
            soma <- soma + idade
            cont <- cont + 1
        fimse
    ate idade = 999
    se cont > 0 entao
        media <- soma / cont
        escreva("Total de alunos: ", cont)
        escreva("Média de idade: ", media:2:2)
    senao
        escreva("Nenhum aluno cadastrado.")
    fimse
    
fimalgoritmo
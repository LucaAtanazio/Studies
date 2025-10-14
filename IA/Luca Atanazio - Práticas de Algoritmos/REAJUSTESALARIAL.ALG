Algoritmo "ReajusteSalarial"

Var
   nome: caractere
   salario, novoSalario, aumento: real
   anos: inteiro
   percentual: real

Inicio
escreva("Nome do funcionário: ")
    leia(nome)
    escreva("Salário atual: R$ ")
    leia(salario)
    escreva("Anos de serviço: ")
    leia(anos)

    se anos <= 3 entao
        percentual <- 0.03
    senao se anos <= 10 entao
        percentual <- 0.125
    senao
        percentual <- 0.20
    fimse

    aumento <- salario * percentual
    novoSalario <- salario + aumento
    
Fimalgoritmo


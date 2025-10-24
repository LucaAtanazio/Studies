algoritmo "ReajusteSalarialComTabela"

var
   salario, novo_salario, diferenca: real
   cargo: inteiro

inicio
   escreval(" Código   Cargo         Percentual     ")
   escreval("   101    Gerente         10%          ")
   escreval("   102    Engenheiro      20%          ")
   escreval("   103    Técnico         30%          ")
   escreval("   Outros Funcionários    40%          ")

   escreva("Digite o salário atual: R$ ")
   leia(salario)
   escreva("Digite o código do cargo (101/102/103): ")
   leia(cargo)

   se cargo = 101 entao
      novo_salario <- salario * 1.10
      escreval("Cargo: Gerente")
   senao
      se cargo = 102 entao
         novo_salario <- salario * 1.20
         escreval("Cargo: Engenheiro")
      senao
         se cargo = 103 entao
            novo_salario <- salario * 1.30
            escreval("Cargo: Técnico")
         senao
            novo_salario <- salario * 1.40
            escreval("Cargo: Outros (40% de aumento)")
         fimse
      fimse
   fimse

   diferenca <- novo_salario - salario

   escreval("Salário antigo: R$ ", salario:8:2)
   escreval("Novo salário:   R$ ", novo_salario:8:2)
   escreval("Diferença:      R$ ", diferenca:8:2)

fimalgoritmo
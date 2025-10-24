Algoritmo "Pesquisa_Valores"

Var
   alunos: vetor[1..5] de caracter
   nome_busca: caracter
   i: inteiro
   encontrado: logico

Inicio
   para i de 1 ate 5 faca
      escreva("Digite o nome do ", i, "º aluno: ")
      leia(alunos[i])
   fimpara

   escreva("Digite o nome que deseja buscar: ")
   leia(nome_busca)

   encontrado <- falso
   para i de 1 ate 5 faca
      se alunos[i] = nome_busca entao
         escreval("Nome encontrado na posição ", i, " do vetor")
         encontrado <- verdadeiro
      fimse
   fimpara

   se nao encontrado entao
      escreval("Nome não encontrado no vetor!")
   fimse
   
Fimalgoritmo

//Pesquisa Valores
//Fazendo operação de soma dos elementos de um vetor desenvolva um algoritmo que leia 5 nomes
//de alunos e os armazene em um vetor chamado alunos.
//Em seguida, solicite ao usuário que insira um nome para buscar no vetor o algoritmo deve
//verificar se o nome esta no vetor e em caso afirmativo, exibir a posição do nome encontrado.
//caso contrario, exibir uma mensagem informando que o nome não foi encontrado

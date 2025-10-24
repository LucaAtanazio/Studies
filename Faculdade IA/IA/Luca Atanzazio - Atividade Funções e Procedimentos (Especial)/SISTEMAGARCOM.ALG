Algoritmo "SistemaGarcom"
//  
//  


Var
   // Usando vetores separados em vez de registro
   nomes: vetor[1..100] de caractere
   salgados: vetor[1..100] de inteiro
   bebidas: vetor[1..100] de inteiro
   qtdClientes, i: inteiro
   nomeCliente: caractere

Funcao NomeSalgado(opcao: inteiro): caractere
Inicio
   escolha opcao
      caso 1: Retorne "Pastel"
      caso 2: Retorne "Coxinha"
      caso 3: Retorne "Quibe"
      caso 4: Retorne "Empada"
      caso 5: Retorne "Enroladinho"
      outrocaso: Retorne "Inválido"
   fimescolha
FimFuncao

Funcao NomeBebida(opcao: inteiro): caractere
Inicio
   escolha opcao
      caso 1: Retorne "Suco"
      caso 2: Retorne "Refrigerante"
      caso 3: Retorne "Água"
      outrocaso: Retorne "Inválido"
   fimescolha
FimFuncao

Procedimento LerCliente(var pos: inteiro)
Inicio
   Escreva("Nome do Cliente: ")
   Leia(nomes[pos])

   Se nomes[pos] <> "sair" entao
      Escreval("Salgados: 1 - Pastel, 2 - Coxinha, 3 - Quibe, 4 - Empada, 5 - Enroladinho")
      Escreva("Salgado: ")
      Leia(salgados[pos])

      Escreval("Bebidas: 1 - Suco, 2 - Refrigerante, 3 - Água")
      Escreva("Bebida: ")
      Leia(bebidas[pos])
   FimSe
FimProcedimento

Procedimento ExibirPedidos()
Var
   i: inteiro
Inicio
   Escreval("Pedidos realizados:")

   Para i de 1 ate qtdClientes faca
      Escreval("Cliente: ", nomes[i])
      Escreval("Salgado: ", NomeSalgado(salgados[i]))
      Escreval("Bebida: ", NomeBebida(bebidas[i]))
      Escreval("-------------------")
   FimPara
FimProcedimento

Inicio
   qtdClientes <- 0

   Repita
      qtdClientes <- qtdClientes + 1
      LerCliente(qtdClientes)

      Se nomes[qtdClientes] = "sair" entao
         qtdClientes <- qtdClientes - 1
         Interrompa
      FimSe
   Ate Falso

   ExibirPedidos()
FimAlgoritmo
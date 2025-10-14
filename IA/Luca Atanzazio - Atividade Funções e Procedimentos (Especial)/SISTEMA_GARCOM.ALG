Algoritmo "SistemaGarcom"
Var
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

Procedimento LerCliente(var indice: inteiro)  // Alterado para "indice"
Inicio
   Escreva("Nome do Cliente: ")
   Leia(nomeCliente)

   Se nomeCliente = "sair" entao
      Retorne
   FimSe

   nomes[indice] <- nomeCliente  // Alterado para "indice"

   Repita
      Escreval("Salgados: 1 - Pastel, 2 - Coxinha, 3 - Quibe, 4 - Empada, 5 - Enroladinho")
      Escreva("Salgado: ")
      Leia(salgados[indice])  // Alterado para "indice"
      Se NomeSalgado(salgados[indice]) <> "Inválido" entao
         Interrompa
      Senao
         Escreval("Opção inválida! Tente novamente.")
      FimSe
   Ate Falso

   Repita
      Escreval("Bebidas: 1 - Suco, 2 - Refrigerante, 3 - Água")
      Escreva("Bebida: ")
      Leia(bebidas[indice])  // Alterado para "indice"
      Se NomeBebida(bebidas[indice]) <> "Inválido" entao
         Interrompa
      Senao
         Escreval("Opção inválida! Tente novamente.")
      FimSe
   Ate Falso
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
   FimPara
FimProcedimento

Inicio
   qtdClientes <- 0

   Repita
      LerCliente(qtdClientes + 1)

      Se nomeCliente = "sair" entao
         Interrompa
      Senao
         qtdClientes <- qtdClientes + 1
      FimSe
   Ate Falso

   ExibirPedidos()
FimAlgoritmo


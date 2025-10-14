"""
Exercício 1 — Busca Sequencial
Título:
Procura de Nome na Lista de Presença
Enunciado:
Uma lista com nomes de alunos foi criada sem nenhuma ordem específica:
alunos = ["Lucas", "Mariana", "Ana", "Pedro", "João", "Beatriz", "Carlos"]
Crie uma função chamada busca_nome(lista, nome_procurado) que utilize
busca sequencial para encontrar o nome do aluno.
 Se encontrar, a função deve retornar o índice onde o nome foi
encontrado.
 Se não encontrar, deve retornar -1.
 Depois, teste seu programa procurando pelos nomes &quot;Ana&quot; e &quot;Thiago&quot;.
Exemplo esperado:
Ana encontrada na posição 2
Thiago não encontrado
"""

def busca_nome(lista, nome_procurado):
    for indice, valor in enumerate(lista):
        if valor == nome_procurado:
            return indice
    return -1

print("Procura de Nome na Lista de Presença:")
alunos = ["Lucas", "Mariana", "Ana", "Pedro", "João", "Beatriz", "Carlos"]
alvo = ["Ana", "Thiago"]

for nome in alvo:
    resultado = busca_nome(alunos, nome) 
    if resultado != -1:
        print(f"\n{nome} encontrado na posição {resultado}")
    else:
        print(f"{nome} não encontrado")

       

        

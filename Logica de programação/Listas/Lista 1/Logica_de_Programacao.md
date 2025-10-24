# **Aula 1 – *Lógica de Programação* (Parte 1)**
## Do básico até a introdução ao *Python*

## 1. **Funções Básicas do Software**
### O que faz um *software*?
Um software realiza processamento de dados — *transforma informações de entrada em informações de saída*.

### *Etapas principais:*
1. **Entrada:** recebe dados do usuário ou de outro sistema.
2. **Processamento:** executa operações sobre esses dados.
3. **Saída:** devolve os resultados ou ações.

```python
# Exemplo simples
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo ao sistema.")

*Saída esperada:*
>> Digite seu nome: Luca
>> Olá, Luca! Seja bem-vindo ao sistema.
```

## 2. *Relações entre as Áreas*
### A programação integra várias áreas fundamentais:
| ***Área***                         | ***Função***                                 | ***Percentual aproximado*** |
| ---------------------------- | -------------------------------------- | --------------------- |
| **Algoritmos**               | Estrutura lógica e sequência de passos | 30%                   |
| **Lógica de Programação**    | Organização e coerência do raciocínio  | 30%                   |
| **Estruturas de Dados**      | Organização eficiente das informações  | 30%                   |
| **Linguagem de Programação** | Implementação prática da lógica        | 10%                   |
Essas áreas se complementam e formam a base de qualquer software.

## 3. *Introdução a **Algoritmos***
### O que é um *algoritmo*?
Um algoritmo é uma sequência finita de passos claros e bem definidos que resolvem um problema.
>> “Procedimento computacional bem definido que toma algum valor como entrada e produz um valor como saída.”
>> — Thomas H. Cormen (2001)

### Exemplo cotidiano: ***Passar café***
1.	*Colocar a água na chaleira*
2.	*Esquentar a água*
3.	*Colocar o filtro na jarra*
4.	*Adicionar o pó de café no filtro*
5.	*Despejar a água quente no filtro*
6.	*Servir o café*
 Mesmo uma tarefa simples segue uma sequência lógica.

```python
def passar_cafe():
    print("1 - Água na chaleira")
    print("2 - Esquentar a água")
    print("3 - Filtro na jarra")
    print("4 - Pó de café no filtro")
    print("5 - Água no filtro")
    print("Café pronto!")

passar_cafe()
```


## 4. ***Lógica de Programação***
Por que é importante?
-	Base de todo raciocínio computacional.
-	Ajuda a resolver problemas de forma estruturada.
-	Facilita a leitura e manutenção do código.

| ***Termo***                | ***Definição***                      |
| -------------------- | ------------------------------- |
| **Instrução**        | Comando ou ação a ser executada |
| **Sequência Lógica** | Ordem correta das instruções    |

###  Exemplo de sequência lógica simples
```python
def fazer_lanche():
    print("1 - Pegar o pão")
    print("2 - Passar manteiga")
    print("3 - Colocar o queijo e o presunto")
    print("4 - Fechar o pão")
    print("5 - Comer! 😋")

fazer_lanche()
```

## 5. Dados e Variáveis
O que é um dado?
Dado é qualquer informação bruta que pode ser armazenada e processada.
Exemplos: número, texto, imagem, endereço, valor, etc.

| ***Tipo***           | ***Característica***                         |
| ------------- | ------------------------------------- |
| **Variável**  | Armazena dados temporários e mutáveis |
| **Constante** | Armazena dados fixos, imutáveis       |

```python
# Variável
idade = 19

# Constantes
PI = 3.14159
GRAVIDADE = 9.8
```

>> Tudo o que é armazenado fica em memória, e variáveis são o meio de acesso a essas informações.

## 6. Introdução ao Python
### ***História***
Criado por *Guido van Rossum* no final dos anos 80.
Lançado em 1991 (versão 0.9.0).
Nome inspirado no grupo de comédia britânico *Monty Python*.
Projetado para ser simples, legível e poderoso.

### ***Características principais***
-	 *Sintaxe simples e clara*
-	 *Altamente versátil*
-	 *Grande comunidade e bibliotecas diversas*
-	 *Interpretado e de alto nível*

### ***Áreas de aplicação***
-	 *Desenvolvimento Web*
-	 *Automação*
-	 *Ciência e Análise de Dados*
-	 *Inteligência Artificial*
-	 *Desenvolvimento de Jogos*

## 7. Sintaxe do Python

### ***Indentação***
O Python usa espaços ou tabulações para definir blocos de código.
Sem a indentação correta, o programa gera erro.

```python
if True:
    print("Indentação correta!")
else:
    print("Indentação incorreta!")

Comentários
# Comentário de uma linha

'''Comentário
de várias linhas'''
```

- *Sensibilidade a maiúsculas/minúsculas*
- *idade, Idade e IDADE são variáveis diferentes.*
- *Ponto e vírgula*

*Opcional — usado se houver múltiplas instruções na mesma linha:*
```python
a = 2; b = 3; print(a + b)
```

## 8. Operadores e Variáveis
### ***Operadores Matemáticos***
| Operador	| Descrição | 
| --------- | --------- | 
| +	| **Adição** | 
| -	| **Subtração** | 
| *	| **Multiplicação** | 
| /	| **Divisão** | 
| //	| **Divisão inteira** | 
| %	| **Resto da divisão** | 
| **	| **Exponenciação** | 

```python
x = 10
y = 3
print(x + y)  # 13
print(x / y)  # 3.333...
print(x // y) # 3
print(x ** y) # 1000
```

### ***Regras de precedência:***

1. **Multiplicação, divisão e resto primeiro.**

2. **Depois adição e subtração.**

3. **Avaliação da esquerda para a direita.**

## 9. Leitura e Escrita de Dados
### **Entrada de dados**
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

Saída de dados
print(f"Olá, {nome}! Você tem {idade} anos.")

Conversões comuns
Tipo	Conversão	Exemplo
Inteiro	int()	int("25")
Decimal	float()	float("3.14")
Texto	str()	str(42)
Booleano	bool()	bool(1) → True
```

## 10. Exercícios Práticos

### **Exiba a mensagem:**
>> "É preciso fazer todos os programas para aprender."
***Leia um número com casa decimal e mostre sua terça parte:***
```python
n = float(input("Digite um número: "))
print(f"A terça parte é {n / 3:.2f}")
```

### ***Leia quatro números inteiros e exiba a soma:***
```python
soma = 0
for i in range(4):
    soma += int(input(f"Digite o {i+1}º número: "))
print("Soma =", soma)
```

### ***Calcule a média ponderada de duas notas (pesos 7 e 3):***
```python
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1*7 + n2*3) / 10
print(f"Média ponderada: {media:.2f}")
```

### ***Exiba dividendo, divisor, quociente e resto:***
```python
a = int(input("Dividendo: "))
b = int(input("Divisor: "))
print(f"{a} / {b} = {a // b} (resto {a % b})")
```
# Conclusões:
- Algoritmos mostram o passo a passo da solução.
- Lógica garante coerência e raciocínio.
- Python transforma teoria em prática.
>> “A prática leva à lógica, e a lógica leva à programação eficiente.”

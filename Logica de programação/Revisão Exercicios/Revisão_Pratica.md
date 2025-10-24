# Revisão – Python

1. **Escreva um programa que solicite ao usuário seu nome e idade, e exiba uma mensagem formatada:**  
   Exemplo de saída:  
   `"Olá, João! Você tem 25 anos."`

2. **Peça ao usuário para digitar dois números e exiba a soma, subtração, multiplicação e divisão formatadas com duas casas decimais.**

3. **Sem utilizar o VSCode, qual o resultado da seguinte expressão em Python?**

4. **Desenvolva um programa que leia três números distintos e informe qual é o maior e qual é o menor.**

5. **Peça ao usuário uma nota de 0 a 10 e exiba um conceito conforme a tabela abaixo:**  

   | Nota | Conceito |
   |------|-----------|
   | >= 9 | A |
   | >= 7 | B |
   | >= 5 | C |
   | >= 3 | D |
   | < 3  | E |

6. **Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago.**  

   Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado:

   | Código | Condição de Pagamento | Desconto/Juros |
   |---------|----------------------|----------------|
   | 1 | À Vista em Dinheiro ou Pix | 15% de desconto |
   | 2 | À Vista no Cartão de Crédito | 10% de desconto |
   | 3 | Parcelado no Cartão em 2x | Sem juros |
   | 4 | Parcelado no Cartão em 3x ou mais | +10% de juros |

7. **Solicite um ano ao usuário e informe se ele é bissexto.**

8. **Crie um sistema de caixa eletrônico que peça ao usuário um valor e exiba a quantidade de cédulas necessárias para sacar esse valor**, considerando notas de **100, 50, 20, 10, 5 e 2.**

9. **Um posto está vendendo combustíveis com a seguinte tabela de descontos:**  
   Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (A - álcool, G - gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo-se que:  
   - Preço do litro da gasolina: **R$ 6,19**  
   - Preço do litro do álcool: **R$ 3,99**

10. **Solicite o peso e a distância de um pacote.**  
    A taxa de frete segue a seguinte lógica:  

    | Peso | Preço por km |
    |-------|----------------|
    | Até 1kg | R$ 5,00 |
    | Entre 1kg e 5kg | R$ 10,00 |
    | Mais de 5kg | R$ 20,00 |  

    Ao final, exiba o custo total.

11. **Crie um programa que funcione como uma calculadora científica.**  
    O usuário deve inserir um número e escolher uma operação entre:

    - `"sqrt"` → Raiz quadrada  
    - `"pow2"` → Elevar ao quadrado  
    - `"pow3"` → Elevar ao cubo  
    - `"log"` → Logaritmo natural (somente para números maiores que zero)  
    - `"exp"` → Exponencial  

    Se o usuário escolher **log** e inserir **zero** ou um **número negativo**, exiba uma mensagem de erro informando que o logaritmo não pode ser calculado.  
    Caso a operação digitada seja inválida, informe ao usuário.

12. **Implemente um programa que leia quatro valores numéricos x, y, z e w e calcule a seguinte expressão matemática:**  

    **Regras:**  
    - O programa deve solicitar ao usuário os valores de x, y, z e w.  
    - Deve garantir que não ocorra divisão por zero. Caso o denominador seja zero, exiba uma mensagem de erro.  
    - O resultado deve ser exibido com quatro casas decimais.  

    **Exemplo:**  
    Entrada: `x = 3, y = 2, z = 4, w = 4`  
    Saída: `E = 9.6742`

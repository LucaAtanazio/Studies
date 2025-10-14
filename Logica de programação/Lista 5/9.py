"""
9. Implemente um programa que receba 10 números inteiros e mostre:
• Os números pares digitados;
• A soma dos números pares digitados;
• Os números ímpares digitados;
• A quantidade de números ímpares digitados;
"""
lista = [int(input(f"{i+1}° numero: ")) for i in range(10)]

par = [num for num in lista if num % 2 == 0]
impar = [num for num in lista if num % 2 != 0]

soma_par = sum(par)
quant_impar = len(impar)

print("\nNúmeros pares na lista:", par)
print("Soma dos números pares:", soma_par)
print("\nNúmeros ímpares na lista:", impar)
print("Quantidade de números ímpares:", quant_impar)
# 17) Construa um algoritmo que indique se um número digitado está compreendido entre
#20 e 90 ou não (20 e 90 não estão na faixa de valores).
n = int(input("Digite um numero: "))

if n > 20 and n < 90 :
    print(f"{n} localizado na faixa 20--90")
else:
    print(f"{n} não localiza na faixa 20--90")
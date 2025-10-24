'''
Levando em consideração a velocidade maxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da velocidade maxima seu programa deve exiber "Não houve multa", caso esteja ate 10km acima, deve exibir: "Levou muita leve", caso esteja entre 11 a 20km acima da velocidade maxima, exibri "levou multa grave", e caso esteja acima de 20km acima da velocidame maxima, exiba: "Levou multa gravissima"
'''

vel_maxima = 80
vel_corrida = float(input("Digite sua velocidade corrida na rodovia: "))

if vel_corrida > vel_maxima and vel_corrida == (vel_maxima+10):
  print("Levou multa leve")
elif vel_corrida > vel_maxima and vel_corrida >= (vel_maxima + 11) and vel_corrida <= (vel_maxima+20) :   
  print("levou multa grave")
elif vel_corrida > vel_maxima and vel_corrida > (vel_maxima+20):   
  print("Levou multa gravissima")
else: 
  print("Não houve multa")
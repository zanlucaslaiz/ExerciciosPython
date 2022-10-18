# Faça um programa que mostre a tabuada de um número que o usuario escolher. 

print ('Tabuada')
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
  print (f'{n} x {c:2} = {n*c}')
  
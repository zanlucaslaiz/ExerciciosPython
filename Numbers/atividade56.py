# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# número primo só é divisivel por 1 e ele mesmo

print ('Número Primo')
cont = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
  if n % i == 0:
    cont += 1

print (f'O número {n} foi dividido {cont} vezes.')

if cont == 2:
    print('Número é primo.')
else:
  print('Número não é primo.')
  
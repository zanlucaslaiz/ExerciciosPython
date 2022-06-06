# crie um programa que leia um numero inteiro e diga se ele é par ou impar.

n = int(input('Digite um numero: '))
resultado = n % 2
if resultado == 0:
  print (f'{n} é um número par.')
else:
  print (f'{n} é um número impar.')
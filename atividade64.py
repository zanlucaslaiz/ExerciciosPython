# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5!= 5x4x3x2x1 120

#from math import factorial
#print('Fatorial')
#n = int(input('Informe um número: '))
#f = factorial(n)
#print(f'O fatorial de {n} é {f}.')

print('Fatorial de n [n!]')
n = int(input('Informe um número: '))
c = n
f = 1
while c > 0:
  print(f'{c} ', end='')
  print('x ' if c > 1 else '= ', end='')
  f *= c
  c -= 1
print(f'O fatorial de {n} é {f}.')

# desafio 63 - escreva um programa que leia o numero n interio qualquer e mostre na tela os n primeiros elementos de uma seguencia de fibonacci:
# 0 1 1 2 2 3 5 6


print('=' * 20)
print('Sequência de Fibonacci')
print('=' * 20)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
cont = 3
while cont <= n:
  t3 = t1 + t2
  print(f'- {t3}', end='')
  t1 = t2
  t2 = t3
  cont += 1
print(' FIM')

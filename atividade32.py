# escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5 e peça para o usuario descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint
c = randint(0,5)
print ('Sortei um número de 0 a 5. Tente adivinhar qual é...')
u = int(input('Qual seu chute:'))
if u == c:
  print ('Você acertou!')
else:
  print ('Você errou!')

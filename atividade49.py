# Desafio 45 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('Vamos jogar Jokenpô?')
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PÔ')

print ('-=' * 20)
print(f'O computador escolheu {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}.')
print ('-=' * 20)

if computador == 0:
  if jogador == 0:
    print ('Empatou!')
  elif jogador == 1:
    print ('Jogador ganhou!')
  elif jogador == 2:
    print ('Computador ganhou!')  
  else:
    print ('Jogada invalida')

elif computador == 1:
    if jogador == 0:
      print ('Computador ganhou!')      
    elif jogador == 1:
      print ('Empatou!')
    elif jogador == 2:
      print ('Jogador ganhou!')
    else:
      print ('Jogada invalida')

elif computador == 2:
    if jogador == 0:
      print ('Computador ganhou!')      
    elif jogador == 1:
      print ('Jogador ganhou!')
    elif jogador == 2:
      print ('Empatou!')
    else:
      print ('Jogada invalida')
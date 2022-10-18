# Melhore o jogo em que o programa vai "pensar" em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessarios para vencer.

from random import randint
print ('Olá jogador.')
c = randint(0,10)
print ('Acabei de pensar em um número entre 0 e 10.')
print ('Tente adivinhar qual foi.')
acertou = False
palpites = 0
while not acertou:
  j = int(input('Qual seu palpite? '))
  palpites += 1
  if j == c:
    acertou = True
  else:
    if j < c:
      print('Mais')
    elif j > c:
      print('Menos')
print('Acertou')
print (f'Para vencer o jogo foram preciso {palpites} palpites.')

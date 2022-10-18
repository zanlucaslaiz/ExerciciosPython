# Faça um programa que jogue par ou impar com o computador. o jogo só será interrompido quando o jogador perder. monstrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint

print('Vamos jogar!')
print('=' * 20)
v = 0
while True:
  j = int(input('digite um valor: '))
  c = randint(0,11)
  total = j + c
  tipo = ' '
  while tipo not in 'PI':
    tipo = str(input('Par ou impar?[P/I]: ')).strip().upper()
  print(f'Você jogou {j} e o computador {c}. total de {total}')
  print('Deu par' if total % 2 == 0 else 'Deu impar')
  if tipo == 'P':
    if total % 2 == 0:
      print('Você ganhou!')
      v += 1
    else:
      print('Você perdeu!')
      break
  elif tipo == 'I':
    if total % 2 == 1:
      print('Você venceu!')
      v += 1
    else:
      print('Você perdeu!')
      break
  print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')

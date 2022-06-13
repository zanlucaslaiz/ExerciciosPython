# Crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte oa usuario qual será o valor a ser sacado (numero inteiro) e o quantas cedulas de cada valor serão entegues.
# obs: considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCO ZANLUCAS'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
  if total >= ced:
    total -= ced
    totalced += 1
  else:
    if totalced > 0:
      print(f'total de {totalced} cedulas de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalced = 0
    if total == 0:
      break
print('Fim da operação')

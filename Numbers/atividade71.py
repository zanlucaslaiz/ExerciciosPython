# Faça um programa que mostre a tabuada de varios números. um de cada vez, para cada valor digitado pelo usuario. o programa será interrompido quando o número solicitado for negativo.

print('=' * 35)
print('TABUADA')
print('=' * 35)

while True:
  n = int(input('Qual número você que ver a tabuada? '))
  if n < 0:
    break
  for c in range(1,11):
    print(f'{n} x {c} = {n*c}')
  print('=' * 30)
print('Fim do programa')
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e os usas respectivas posições na lista.

num = list()
for n in range(0,5):
  num.append(int(input('Digite um valor: ')))
print(f'Os números digitados foram: {num}')
print(f'O maior número digitado foi {max(num)} na posição {num.index(max(num))+1}')
print(f'O menor número digitado foi {min(num)} na posição {num.index(min(num))+1}')

'''# solução do video
listanum = []
mai = 0
men = 0
for c in range(0, 5):
  listanum.append(int(input(f'Digite um valor para a posição {c}:' )))
  if c == 0:
    mai = listanum[c]
  else:
    if listanum[c] > mai:
      mai = listanum[c]
    if listanum[c] < men:
      men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
  if v == mai:
    print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições, ', end='')
for i, v in enumerate(listanum):
  if v == men:
    print(f'{i}...', end='')
print()
'''
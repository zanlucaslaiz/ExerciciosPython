# Faça um programa que leia nome e peso de varias pessoas. Guardando tudo em uma lista. No final mostre:
# A) quantas pessoas foram cadastradas 
# B) uma listagem com as pessoas mais pesadas.
# C) uma listagem com as pessoas mais leves

temp = []
dados = []
mai = men = 0
while True:
  temp.append(str(input('Digite o nome: ')))
  temp.append(float(input('Digite o peso: ')))
  if len(dados) == 0:
    mai = men = temp[1]
  else:
    if temp[1] > mai:
      mai = temp[1]

    if temp[1] < men:
      men = temp[1]
  dados.append(temp[:])
  temp.clear()
  resp = str(input('Quer continuar? ')).strip().upper()
  if resp in 'Nn':
    break

print(f'foram cadastrado {len(dados)} pessoas.')
print(f'O maior peso foi {mai} kilos. Peso de ', end='')
for p in dados:
  if p[1] == mai:
    print(f'[{p[0]}]')
print(f'O menor peso foi {men} kilos. Peso de ', end='')
print()
for p in dados:
  if p[1] == men:
    print(f'[{p[0]}]')
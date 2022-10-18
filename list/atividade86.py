# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso. Crie duas listas extras que vão contar apenas os valores pares e o valores impares digitados, respectivamente. Ao final, mostre o conteúdo das tres listas geradas.

num = []
pares = []
impares = []
while True:
  num.append(int(input('Digite um número: ')))
  resp = str(input('Quer continuar?[S/N]: '))
  if resp in 'Nn':
    break
for i,v in enumerate(num):
  if v % 2 == 0:
    pares.append(v)
  elif v % 2 == 1:
    impares.append(v)
print('-=' * 30)
print(f'A lista de completa é {num}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de impares {impares}.')
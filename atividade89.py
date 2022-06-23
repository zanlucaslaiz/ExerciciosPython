# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre- os em uma lista unica que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

n = [[],[]]
valor = 0

for i in range(1,8):
  valor = int(input('Digite um valor: '))
  if valor % 2 == 0:
    n[0].append(valor)
  else:
    n[1].append(valor)
n[0].sort()
n[1].sort()
print(f'valores pares: {n[0]}')
print(f'valores impares: {n[1]}')
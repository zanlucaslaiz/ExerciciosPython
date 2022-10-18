# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final. Mostre: 
# A - quantas vezes apareceu o valor 9.
# B - em que posição foi digitado o primeiro valor 3.
# C - quais foram os numeros pares.

n = (int(input(f'Digite o 1º número: ')), 
int(input(f'Digite o 2º número: ')), 
int(input(f'Digite o 3º número: ')),
int(input(f'Digite o 4º número: ')))
print(f'Os números digitados foram: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
  print(f'O número 3 foi digitado primeiro no posição {n.index(3)+1}.')
else:
  print('O número três não foi digitado')
for i in n:
  if i % 2 == 0:
    print(f'{i}', end=' ')
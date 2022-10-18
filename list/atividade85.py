# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso. Mostre: 
# a) quantos números foram digitados.
# B) a lista de valores, ordenanda de forma descrecente.
# C) se o valor 5, foi digitado e esta ou não na lista

num = []
while True:
  num.append(int(input('Digite um valor: ')))
  resp = str(input('Quer continuar?[S/N]: ')).upper()
  if resp == 'N':
    break
print(f'Você digitou {len(num)}.')
num.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente: {num}')
if 5 in num:
  print('O número 5 está na lista.')
else:
  print('O número 5 não está na lista.')
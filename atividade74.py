# Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuario vai continar. No final, mostre:
# A- qual é o total gasto na comprar.
# B- quantos produtos custam mais de R$ 1000.
# C- qual é o nome do produto mais barato.

print('-' * 30)
print('LOJAS ZANLUCAS')
print('-' * 30)
totalc = maisMil = menor = cont = 0
barato = 0
while True:
  produto = str(input('Qual o produto? ')).strip()
  valor = float(input('Qual valor?R$ '))
  cont +=1
  totalc += valor
  if valor > 1000:
    maisMil += 1
  if cont == 1 or valor < menor:
    menor = valor
    barato = produto
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Quer continuar?[S/N] ')).upper()[0].strip()
  if continuar == 'N':
    break

print(f'Total da comprar foi: {totalc:.2f}')
print(f'Temos {maisMil} produtos custam mais de R$1000.')
print(f'O produto {barato} com o valor {menor:.2f} é o mais barato.')

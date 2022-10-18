# Crie uma programa que leia o ano de nascimento de sete pessoas no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(1,8):
  nasc = int(input('Digite o ano de nascimento: '))
  idade = atual - nasc
  if idade >= 18:
    maior += 1
  else:
    menor += 1
print(f'Temos {maior} pessoas maior de idade.')
print(f'Temos {menor} pessoas menor de idade.')

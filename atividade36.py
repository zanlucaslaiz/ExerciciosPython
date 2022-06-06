# faça um programa que leia um ano qualquer é mostre se ele é bisexto

from datetime import date
ano = int(input('Digite o ano: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print (f'O ano {ano} é bisexto.')
else:
  print (f'O ano {ano} não é bisexto')
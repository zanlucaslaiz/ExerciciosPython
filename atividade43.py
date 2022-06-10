# Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade: - se ainda vai se alistar os serviço militar. 
# - se e a hora de se alistar. 
# - se ja passou do tempo do alistamento. 
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print (f'Quem nasceu em {nasc} tem {idade} anos, em {atual}.')
if idade == 18:
  print ('Você precisa se alistar.')
elif idade < 18:
  saldo = 18 - idade
  print (f'Ainda falta {saldo} anos para você se alistar.')
  ano = atual + saldo
  print (f'Seu alistamento será em {ano} ano.')
elif idade > 18:
  saldo = 18 - idade
  print (f'Você já deveria ter se alistado há {saldo} anos.')
  ano = atual - saldo
  print (f'Seu alistamento foi em {ano}.')
  
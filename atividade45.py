# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
# até 9 anos: mirim,
# até 14 anos: infantil,
# até 19 anos: junior,
# até 20 anos: senior,
# acima: master.

from datetime import date
atual = date.today().year
print ('Verifique a categoria do atleta.')
an = int(input('Digite o ano de nascimento: '))
idade = atual - an

if idade <= 9:
  print ('MIRIM')
elif idade <= 14:
  print ('INFANTIL')
elif idade <= 19:
  print ('JUNIOR')
elif idade <= 20:
  print ('SENIOR') 
else:
  print ('MASTER')


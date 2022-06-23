# Crie um programa que tenha um tupla com varias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Banana', 'Abacate', 'Caqui', 'Melancia', 'Abacaxi', 'Laranja' )
for i in palavras:
  print(f'\nNa palavra {i.upper()} temos as vogais: ', end='')
  for l in i:
    if l.upper() in 'AEIOU':
      print(l, end=' ')
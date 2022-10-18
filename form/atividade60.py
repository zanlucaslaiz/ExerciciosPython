# Desenvolva uma programa que leia o nome, idade, e sexo de 4 pessoas. no final do programa, mostre:
# - a media de idade do grupo.
# - Qual é o nome do homem mais velho.
# - quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1,5):
  print (f'----- {p}ª pessoa -----')
  nome = str(input(f'Digite o nome: ')).strip()
  idade = int(input(f'Digite a idade: '))
  sexo = str(input(f'Digite o sexo [M/F]: ')).strip()
  somaidade += idade
  if p == 1 and sexo in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    totalmulher20 += 1
mediaidade = somaidade / 4
print (f'A média de idade do grupo é {mediaidade}.')
print (f'O Nome do mais velho {nomevelho} e tem {maioridadehomem}.')
print (f'Ao todo são {totalmulher20} mulheres menor que 20 anos.')
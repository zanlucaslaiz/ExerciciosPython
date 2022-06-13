# Crie um programa que leia a idade o sexo de varias pessoas. a cada pessoa cadastrada. o programa deverá perguntar se o usuario quer ou não continuar. no final mostre: 
# a - quantas pessoas tem mais de 18 anos.
# b - quantos homens foram cadastrados.
# c - quantas mulheres tem menos de 20 anos.

total18 = totalm = totalm20 = 0
while True:
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Sexo[M/F]: ')).upper()[0].strip()
  if idade >= 18:
    total18 += 1
  if sexo == 'M':
    totalm += 1
  if sexo == 'F' and idade < 20:
    totalm20 += 1
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar?[S/N]:  ')).strip().upper()[0]
  if resp == 'N':
    break
print(f'Total de pessoas maiores de 18: {total18}')
print(f'Total de homens cadastrado: {totalm}')
print(f'Total de mulheres com menos de 20 anos: {totalm20}')
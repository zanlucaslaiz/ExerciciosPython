# Faça um programa que leia nome e media de um aluno, guardando também o situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
  aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
  aluno['Situação'] = 'Reprovado'
else:
  aluno['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
  print(f'   - {k} é igual a {v}.')

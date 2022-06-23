# desafio 92 - crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO. O dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade. Com quantos anos a pessoas vai se aposentar.

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
  dados['contratação'] = int(input('Ano de contratação: '))
  dados['salário'] = float(input('Salário: R$ '))
  dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
  print(f'    - {k} vai se aposentar com {v} anos.')
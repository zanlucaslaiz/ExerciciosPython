# desafio 022
# crie um programa qu leia o nome completo de uma pessoa:
# o nome com todas as letra maiusculas
# o nome com todas as letras minusculas
# quantas letras tem ao todo (sem contar espaços)
# quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analizado seu nome...')
print(f'Seu nome em maiuscula: {nome.upper()} ')
print(f'Seu nome em minuscula é {nome.lower()} ')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
# print(f'O seu primeiro nome tem {nome.find(" ")} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
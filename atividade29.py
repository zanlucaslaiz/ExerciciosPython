# crie um programa que leia o nome de uma pessoa e diga se tem o nome "silva"

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Esse nome tem silva?{("SILVA" in nome.upper())}')
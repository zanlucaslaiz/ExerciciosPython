# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo  nome separado.

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'O primeiro nome é: {n[0]}')
print(f'O último nome é: {n[len(n,)-1]}')

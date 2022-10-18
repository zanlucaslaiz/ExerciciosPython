# Faça um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('gerador de pa')
print('-=' * 10)
t = int(input('digite o termo: '))
razao = int(input('digite a razão: '))
termo = t
cont = 1
while cont <= 10:
    print(f'{termo} - ', end= ' ')
    termo += razao
    cont += 1
print('fim')
# desafio 23
# faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separado
# unidade dezena centena milhar

num = int(input('Informe um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O número digitado foi {num} \nUnidade: {u}; \nDezena: {d}; \nCentena: {c}; \nMilhar: {m}.')


# cria um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
n = float(input('digite um número: '))

print(f'O Valor digitado foi {n} e sua parte inteira é {trunc(n)}.')

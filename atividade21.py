# faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de uma  triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# co = float(input('Digite o cateto oposto: '))
# ca = float(input('Digite o cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)

# print (f'O comprimento da hipotenusa é {hi:.2f}:')

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co,ca)
print (f'O comprimento da hipotenusa é {hi:.2f}:')
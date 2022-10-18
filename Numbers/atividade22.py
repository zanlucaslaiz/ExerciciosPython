# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite o angulo: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print(f'Para o angulo {an}. \nO seno é {se:.2f}. \nO conseno é {co:.2f}. \nA tangente é {tan:.2f}.')

# from math import sin, cos, tan, radians
# an = float(input('Digite o angulo: '))
# se = sin(radians(an))
# co = cos(radians(an))
# tan = tan(radians(an))

# print(f'Para o angulo {an}. \nO seno é {se:.2f}. \nO conseno é {co:.2f}. \nA tangente é {tan:.2f}.')
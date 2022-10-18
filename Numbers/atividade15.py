# faça um programa que leia a altura e largura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².

larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'A area a ser pintada é {area}.')
print(f'Para pintar essa area você precisara de {tinta} litros de tinta.')


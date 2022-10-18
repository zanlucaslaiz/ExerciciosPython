# desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou não formar um triangulo.
# se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
  print ('Os três segmentos PODEM formar um triangulo.')
else:
  print ('Os três segmentos NÃO PODEM formar um triangulo.')
# Faça um programa que mostre que tipo de triangulo será formado: 
# equilatero: todos lados sao iguais, 
# isoceles: dois lados iguais, 
# escaleno: todos os lados diferente.

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
  print ('Os três segmentos PODEM formar um triângulo', end='')
  if r1 == r2 == r3:
    print ('EQUILATERO.')
  elif r1 == r2 or r2 == r3 or r3 == r1:
    print ('ISOCELES.')
  elif r1 != r2 != r3 != r1:
    print ('ESCALENO.')
else:
  print ('Os três segmentos NÃO PODEM formar um triângulo.')




# escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade: '))
limite = velocidade - 80
multa = limite * 7.00
if velocidade > 80:
  print (f'Você foi utrapassou {limite} km/h e foi multado em {multa} reais.')

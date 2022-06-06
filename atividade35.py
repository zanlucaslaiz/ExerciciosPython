# desenvolva um programa que pergunte a distancia de uma viagem em kilometros, calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.

d = float(input('Digite a kilometragem do seu destino: '))
if d <= 200:
  t1 = d * 0.50
  print (f'Sua viagem tem {d} km e vai custar {t1:.2f} reais.')
else:
  t2 = d * 0.45
  print (f'Sua viagem tem {d} km e vai custar {t2:.2f} reais.')

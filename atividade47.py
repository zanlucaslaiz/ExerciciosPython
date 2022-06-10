# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule o seu IMC e mostre seu status. de acordo com:
# abaixo de 18.5: abaixo do peso, 
# entre 18.5 e 25: peso ideal, 
# 25 ate 30: sobrepesso, 
# 30 ate 40: obesidade, 
# acima de 40: obesidade morbida.

print ('Teste seu IMC')
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print (f'O seu IMC é {imc:.1f}')
if imc < 18.5:
  print ('Abaixo do peso.')
elif 18.5 <= imc < 25:
  print ('Peso ideal.')
elif 25 <= imc < 30:
  print ('Sobrepeso.')
elif 30 <= imc < 40:
  print ('Obesidade.')
else:
  print ('Obesidade Morbida.')
# Crie o programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. ( desconsiderando o flag)

print('Somando valores')
print('=' * 30)
n = cont = soma = 0
n = int(input('Digite um valor[digite 999 para parar]: '))
while n != 999:
  soma += n
  cont += 1
  n = int(input('Digite um valor[digite 999 para parar]: '))
print(f'Foi digitado {cont} números e a soma deles é {soma}.')

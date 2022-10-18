# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = cont = 0
while True:
  n = int(input('Digite um valor (999 para parar): '))
  if n == 999:
    break
  cont += 1
  soma += n
print(f'A soma de {cont} números é {soma}.')


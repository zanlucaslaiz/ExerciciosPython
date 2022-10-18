# Crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em um lista. Caso o número já exista la dentro. Ele não será adicionado. No final serão exibidos todos os valores unicos digitados. Em ordem crescente.

numeros = list()
n = 0
while True:
  n = (int(input('Digite um numero: ')))
  if n not in numeros:
    numeros.append(n)
  else:
    print('Valor já existe!')
  resp = str(input('Quer continuar?[S/N]: '))
  if resp in 'Nn':
    break
numeros.sort()
print(numeros)


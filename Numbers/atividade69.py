# Crie um programa que leia varios numeros interios pelo teclado. No final da execução. Mostre media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
  n = int(input('Digite o número: '))
  soma += n
  quant += 1
  if quant == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    elif n < menor:
      menor = n
  resp = str(input('Quer continuar a digitar[S/N]')).upper()[0].strip()
media = soma / quant
print(f'Foi digitado {quant} numeros e a media foi {media}.')
print(f'o maior numero é {maior} e o menor é {menor}.')
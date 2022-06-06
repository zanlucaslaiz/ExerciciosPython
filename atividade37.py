# faça um programa que leia três numeros e mostre qual o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print (f'O número {maior} é maior. \n O número {menor} é menor.')
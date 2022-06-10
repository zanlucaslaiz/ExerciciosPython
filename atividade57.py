# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo. desconsiderando os espaços.
# Ex: Apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
if inverso == junto:
  print ('Essa frase é um palindromo.')
else:
  print ('Essa frase não é um palindromo.')
  
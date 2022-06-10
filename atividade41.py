# Escreva um programa que leia  numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão: 1 para binario, 2 para octal, 3 hexadecimal.
# procurar o video de bases numericas.

n = int(input('Digite um número inteiro:'))
print ('''Escolha umas das bases de conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Digite sua oção: '))
if opcao == 1:
  print (f'{n} convertido para binario é {bin(n) [2:]}.')
elif opcao == 2:
  print (f'{n} convertido para octal é {oct(n) [2:]}.')
elif opcao == 3:
  print (f'{n} convertido para hexadecimal é {hex(n) [2:]}')
else:
  print ('Opção invalida.')
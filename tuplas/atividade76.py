# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero','um', 'dois', 'três','quatro', 'cinco', 
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resp = ''
while True:
  n = int(input('Digite um número entre 0 e 20: '))
  resp = str(input('Quer continuar?[S/N]')).upper()
  if 0 <= n <= 20:
    break
  print('Tente novamente: ', end='')
print(f'O número {n} por extenso é {num[n]}')

# fazer perguntar se quer escolher outro numero.
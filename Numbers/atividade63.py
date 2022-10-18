# Crie um programa e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
print('Calculando.')
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opcao = 0
while opcao != 5:
  print('''  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos números
  [5] Sair do programa''')
  opcao = int(input('Escolha uma opção: '))
  if opcao == 1:
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é {soma}.')
  elif opcao == 2:
    produto = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é {produto}.')
  elif opcao == 3:
    if n1 > n2:
      maior = n1
      print(f'O maior numero é {maior}.')
    elif n2 > n1:
      maior = n2
      print(f'O maior numero é {maior}.')  
  elif opcao == 4:
    print('Informe os números novamente')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))  
  elif opcao == 5:
    print('Finalizando...')  
  else:
    print('Opção invalida. Tente de novo.')
  print('=-=' * 10)
  sleep(2)
print('Fim do programa.')

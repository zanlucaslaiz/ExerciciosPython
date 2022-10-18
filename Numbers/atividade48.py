# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - á vista dinheiro/cheque: 10% de desconto.
# - á vista no cartão: 5% de desconto.
# - 2x no cartão: preço normal.
# - 3x ou mais no cartão: 20% de juros.

print('LOJAS ZANLUCAS')
preco = float(input('Digite o valor total do produto: R$ '))
print('''Calculando o desconto.
Digite o valor do produto e depois escolha uma forma de pagamento:
[ 1 ] á vista no dinheiro/cheque.
[ 2 ] á vista no cartão.
[ 3 ] em até 2x no cartão.
[ 4 ] 3x ou  mais no cartão.''')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parc = total/2
    print(f'Sua compra será parcelada em 2x de {parc:.2f}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parc = total / totalparc
    print(f'Sua compra será divida em {totalparc}x de R${parc:.2f} com juros.')
else:
  total = 0
  print ('Opção de pagamento invalida.')
print(f'O valor do produto era R${preco:.2f} vai custar R${total:.2f}.')


# Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
print(f'{"TABELA DE PREÇO":^40}')
print('-' * 40)
produtos = ('caderno', 10.50, 
'caneta', 1.50, 
'lapiz', 1.00, 
'borracha', 2.00, 
'apontador', 4.00)
for i in range(0, len(produtos)):
  if i % 2 == 0:
    print(f'{produtos[i]:.<30}', end=' ')
  else:
    print(f'R${produtos[i]:>7.2f}')

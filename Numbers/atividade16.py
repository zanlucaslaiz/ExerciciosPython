# faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

preco = float(input('qual o preço do produto?  R$ '))
novo = preco - (preco * 5 / 100)
print(f'O produto que custava R$ {preco:.2f} na promação vai custar R$ {novo:.2f}.')
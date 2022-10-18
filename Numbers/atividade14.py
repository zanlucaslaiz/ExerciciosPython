# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares é pode comprar
# 1 dollar = 5,13 informação em 12/05/2022

r = float(input('Digite qual o valor que pretende gastar: R$ '))
d = float(input('Digite o valor do dollar atual: '))
q = float(r / d)
print(f'Com {r} é possivel comprar {q:.2f} dollares')
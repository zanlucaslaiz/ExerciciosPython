# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi aluguado. Calcule o preço a pagar. Sabendo que o carro custa R$ 60 por dia a R$ 0.15 por km rodados.

km = float(input('digite os kilometros percorridos: '))
d = float(input('digite quantos dias ficou com o carro: '))
tk = km * 0.15
td = d * 60
total = tk + td
print(f'O valor a ser pago pelos kilometros percorridos R$ {tk}.')
print(f'O valor a ser pago das diarias é R$ {td}.')
print(f'O valor total a ser pago é R$ {total}.')
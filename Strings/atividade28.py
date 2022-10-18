# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

cid = str(input('Digite o nome da sua cidade: ')).strip()
print (f'A cidade começa com santo?{cid[:5].upper() == "SANTO"}')


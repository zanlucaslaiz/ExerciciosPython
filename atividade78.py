# Crie um programa que vai gerar cincos numeros aleatórios e colocar em uma tupla. Depois disso, mostre a listagem do números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números sorteados foram: {n}')
print(f'O maior número foi: {max(n)}')
print(f'O menor número foi: {min(n)}')
# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada

x = int(input('Digite um número: '))
d = x * 2
t = x * 3
rq = x**(1/2)
print(f'O dobro de {x} é {d}. \nO triplo de {x} é {t}. \nA raiz quadrada de {x} é {rq:.2f},')
# outra forma de calcular a raiz quadrada é pow(n, (1/2))


# prefessor que sortear um dos seus quatro aluno para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendoo nome escolhido.

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno sorteado foi {escolhido}.')

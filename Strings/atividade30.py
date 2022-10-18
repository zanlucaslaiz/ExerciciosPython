# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece pela primeira vez
# em que posição ela aparece pela ultima vez

frase = str(input('Digite um frase: ')).upper().strip()
print(f'A letra "a" aparece {frase.count("A")} vezes.')
print(f'A primeira vez na posição {frase.find("A")+1}.')
print(f'A ultima vez na posição {frase.rfind("A")+1}.')

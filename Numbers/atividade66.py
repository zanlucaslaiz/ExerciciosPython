# melhore a atividade 65. Perguntando para o usuario se ele quer  mostrar mais alguns termos. O programa encerra quando ele disser quer mostrar 0 termos.

print('gerador de pa')
print('-=' * 10)
t = int(input('digite o termo:  '))
razao = int(input('digite a razão: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ', end= ' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('fim')
print(f'progressao finalizada com {termo} termos.')
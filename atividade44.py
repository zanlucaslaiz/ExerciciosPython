# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final. de acordo com a media atingida:
# media abaixo 5.0 : reprovado.
# media entre 5.0 e 6.9 : recuperacao.
# media 7.0 ou superior: aprovado.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'sua nota é {m}.')
if m < 50:
    print('Você foi reprovado!')
elif 70 > m >= 50:
    print('Você está de recuperação!')
else:
    print('Você foi aprovado!')
    
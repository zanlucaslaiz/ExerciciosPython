# Escreva  programa para aprovar o emprestimo de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

print('Calculando seu emprestimo.')
vc = float(input('Digite o valor da casa: R$ '))
s = float(input('Qual a renda do comprador? R$ '))
a = int(input('Quantos anos de pagamento? '))
vp = vc / (a * 12)
p = s * 70 / 100
print (f'Para pagar uma casa de R${vc:.2f} em {a} anos o valor da parcela será {vp:.2f}.')
if vp <= p:
    print('Parabéns! Seu empréstimo foi aprovado!')
else:
    print('Sinto muito! Seu empréstimo foi negado!')

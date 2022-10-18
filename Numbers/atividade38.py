# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. para salario superior a R$ 1250,00. calcule um aumento de 10%. para os inferiores ou iguais o aumento é de 15%

salario = float(input('Digite seu salário: '))
if salario <= 1250.00:
  novo = salario + (salario * 15 / 100)
else:
  novo = salario + (salario * 10 / 100)
print (f'Quem ganhava {salario} reais passa a ganhar {novo} reais.')
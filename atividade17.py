# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('salario atual: R$ '))
novo = salario + (salario * 15 / 100)
print(f'O salario do funcionario vai de R$ {salario} para R$ {novo}.')

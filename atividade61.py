# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores M ou F. Caso esteja errado. Peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [F/M]: ')).upper()[0].strip()
while sexo not in 'MF':
  sexo = str(input('Opção invalida. Por fovar escolha entre a duas opções válidas: ')).upper()[0].strip()
print(f'O sexo informado foi {sexo}.')
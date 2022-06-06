# escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
# 1 metro = 100 centrimetros = 1000 milimetros
# km hm dam m dm cm mm
m = float(input('Digite uma ditância em metro: '))
km = float(m / 1000)
hm = float(m / 100)
dam = float(m / 10)
dm = float(m * 10)
cm = float(m * 100)
mm = float(m * 1000)
print(f'{m} é igual a \n{km} kilometros. \n{hm} hm. \n{dam} dam. \n{dm} dm. \n{cm} centimetro. \n{mm} milimetros.')



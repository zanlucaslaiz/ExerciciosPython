# operações aritméticos
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisãointeira
# % Resto da divisão
# == igual


# operando:  todo operador precisa de um operando, pode ser um numero, pode ser uma string ou até mesmo uma variavel. No dos operadores aritiméticos somemente numeros e variaveis que conte nuemros.
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

# ordem de precedencia

# 1   ( )
# 2   **
# 3   * / // %
# 4   + -

# 5+3*2==11
# 3*5+4**2==31
# 3*(5+4)**2==243

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# caso queira definir o numero de casas decimais {:.2f}
print(f'A soma é {s}, o produto é {m} e a divisão é {d}')
print(f'Divisão inteira é {di} e a potencia {e}')
# para evitar que a linha se quebre colocar , end=' '
# para fazer outra linha \n

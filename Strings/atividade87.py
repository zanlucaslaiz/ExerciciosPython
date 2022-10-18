# Crie um programa onde o usuário digite uma expressão qualquer que usa parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.


ex = str(input('Digite uma expressão: '))
pilha = []
for simb in ex:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua expressão está válida.')
else:
  print('Sua espressão está inválida.')

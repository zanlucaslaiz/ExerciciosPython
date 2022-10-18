# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol, na ordem de colocação.  Depois mostra: 
# A - apenas os 5 primeiros colocados.
# B - os últimos 4 colocados.
# C - uma lista com os times em ordem alfabética
# D - em que posição está o time da Ceara.

times = ('Palmeiras', 'Corinthians', 'São paulo', 'Internacional', 'athletico-pr', 'Atletico-mg', 'Coritiba', 'Fluminense', 'América-mg', 'Avai', 'Santos', 'Red bull bragantino', 'Ceara', 'Goias', 'Atletico-go', 'Flamengo', 'Botafogo', 'Cuiaba', 'Junventude', 'Fortaleza')

print(f'Lista de times {times}')
print('=' * 30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=' * 30)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('=' * 30)
print(f'Ordem alfabetica{sorted(times)}')
print('=' * 30)
print(f'O Ceará está na posição {times.index("Ceara")+1}.')


#Tabela do futebol brasileiro
tabela = ('Internacional','Flamengo','Atlético-MG','Fluminense','São Paulo','Santos','Palmeiras','Fortaleza','Grêmio','Ceará','Atlético-GO','Sport', 'Corinthians','Bahia','Bragantino','Botafogo','Vasco','Athletico-PR','Coritiba','Goiás')
print(f'Os cinco primeiros são: {tabela[0:5]}')
print(f'Os quatro ultimos são: {tabela[-4:]}')
print(f'Em ordem alfebetica a tabela fica: {sorted(tabela)}')
print(f'O Santos está na posição: {tabela.index("Santos"+1)}')
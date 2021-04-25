def ficha(name = '<Desconhecido>',gols = 0):
    """
    -> Função para mostrar a ficha de um jogador
    :param name: (opcional) mostra o nome do jogador
    :param gols: (opcional)mostra a quantidade de gols
    """
    print(f'O jogador {name} fez {gols} gols no campeonato')

n = str(input('Nome do jogador: '))    
g = str(input('Quantidades de gol: '))
if g.isnumeric():
    g = int(g)
else:
    g= 0    
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
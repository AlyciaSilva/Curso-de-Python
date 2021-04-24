#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gools = list()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas jogou?'))
for num in range (0, partidas):
    gools.append(int(input(f'=> Quantos gools na partida {num}?')))
jogador['gols'] = gools.copy()
jogador['total'] = sum(gools)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for num in range(0,partidas):
    print(f'    => Na partida {num}, fez {gools[num]} gols.')
print(f'Foi um total de {jogador["total"]} gols')
#Crie um programa que gerencie o aproveitamento de vários jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
time = list()
gools = list()
while True:
    jogador.clear()
    gools.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas jogou?'))
    for num in range (0, partidas):
        gools.append(int(input(f'=> Quantos gools na partida {num}?')))
    jogador['gols'] = gools.copy()
    jogador['total'] = sum(gools)
    time.append(jogador.copy())
    resp = str(input('Desejar inserior outro jogador? (S/N)')).upper()
    while resp != 'N' and resp != 'S':
        print('Erro! Digite apenas S ou N')
        resp = str(input('Desejar inserior outro jogador? (S/N)')).upper() 
    if resp == 'N':
        break
print('=-'*30)
print('   Cod   Nome         Gols        Total')
print('=-'*30)    
for k,v in enumerate(time): 
    print(f'{k:>5} ', end= "")
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()    
print('=-'*30)
while True:
    pergunta = int(input('Mostrar o levantamento de qual jogador? 999 para parar'))
    if pergunta == 999:
        break
    if pergunta > len(time):
        print('Número inválido')
    else:
        print(f'Levantamento do jogador {time[pergunta]["Nome"]}')
        for p,g in enumerate(time[pergunta]["gols"]):
            print(f'No jogo {p} foram {g} gols')
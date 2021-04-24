#quatro números de um dado 
import random, time 
from operator import itemgetter
jogo = {'jogador1': random.randint(1,6),
        'jogador2': random.randint(1,6),
        'jogador3': random.randint(1,6),
        'jogador4': random.randint(1,6)}
score = list()
cont = 1
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'O {k} tirou {v} no dado!')
    time.sleep(1)
score = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print("=-"*30)
print('  '*30)
print('== O RANKING DE JOGADORES ==')
for chave, colocados in enumerate(score):
    print(f'{chave+1}° lugar: {colocados[0]} com {colocados[1]}')
    time.sleep(1)
        

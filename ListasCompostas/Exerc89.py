#gerar palpites de 1 a 60
import random, time
lista = list()
palpite = list()
cont = 0
print('=-='*30)
print('Bem vindo ao programa gerador de palpites')
print('=-='*30)
numPalpites = int(input('Quantos jogos deseja gerar? '))
while len(lista) != numPalpites:
    while len(palpite) != 6:
        valor = random.randint(1 ,60)
        if valor not in palpite:
            palpite.append(valor)
    palpite.sort()
    if palpite not in lista:
        lista.append(palpite[:])
        palpite.clear()
    print(f'Jogo {cont+1}: {lista[cont]}')
    cont += 1
    time.sleep(1)
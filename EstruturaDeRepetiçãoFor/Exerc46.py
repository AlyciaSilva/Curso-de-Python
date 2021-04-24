#CONTAGEM REGRESSIVA com 1s de espera
from time import sleep
print('Contatgem regressiva para os fogos!!!')
print('-------------------------------------')
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('FOGOS!!!!!!!!!!!!')    
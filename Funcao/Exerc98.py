#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada
import time
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        while cont <= f  :
                print(f'{cont} ', end ='', flush = True)
                time.sleep(0.5)
                cont += p
        print('Fim!')
    else:
        while cont >= f  :
                print(f'{cont} ', end ='', flush = True)
                time.sleep(0.5)
                cont -= p
        print('Fim!')
    print('--'*30)
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))
contador(inicio,fim,passo)
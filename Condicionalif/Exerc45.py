#Jogo de pedra papel e tesoura
import random
def resultado (a,b):
    if escolha != 1 and escolha != 2 and escolha != 3:
        print('Numero inválido')
    else:
        if lista[a] == b - 1:
            print('Empate!!!')
        elif lista [a] == lista[0] and escolha == 2: #usuário ganha
            print('Parabéns, você ganhou!!')
        elif lista [a] == lista[1] and escolha == 1: #máquina ganha
            print('Você perdeu!!')        
        elif lista [a] == lista[2] and escolha == 1: #usuário ganha
            print('Parabéns, você ganhou!!')
        elif lista [a] == lista[0] and escolha == 3:# máquina ganha
            print('Você perdeu!!')       
        elif lista [a] == lista[1] and escolha == 3:#usuário ganha
            print('Parabéns, você ganhou!!')
        elif lista [a] == lista[2] and escolha == 2:#máquina ganha
            print('Você perdeu!!')       

print('Jogo de jokenpo')
escolha = int(input('Pedra, papel ou tesoura? \n (1) Pedra \n (2) Papel\n (3)Tesoura: '))
lista = ['Pedra', 'Papel', 'Tesoura']
sorteado = random.randint(0,2)
print(1)
print(2)
print(3)
print("E")
resultado(sorteado,escolha)
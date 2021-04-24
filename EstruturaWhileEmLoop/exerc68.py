#Impar ou par, jogo será executado até o jogador perder 
import random
print('Jogo de impar ou par')
cont = 0
while True:
    num = int(input('Digite um número: '))
    resp = str(input('Você quer impar ou par? I para impar e P para par: ')).upper()
    pc = random.randint(0,9998)
    soma = num + pc
    print(soma)
    if soma % 2 == 0 and resp == "P":
        print('Você ganhou')
        cont += 1
    elif soma % 2 == 0 and resp == "I":
        print('Você perdeu!!')
        break
    elif soma % 2 != 0 and resp == "I":
        print('Você ganhou')
        cont += 1
    elif soma % 2 != 0 and resp == "P":    
        print ('Você perdeu!!')
        break
print (f'Você ganhou {cont} vez(es)')
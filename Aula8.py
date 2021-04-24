#Aprendendo a usar bibliotecas
#from math import sqtr (importa apenas uma função da biblioteca math)
import math, random, emojis
num = int(input('Digite um número: '))
#raiz = sqrt (num)
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}!!'.format(num, raiz))
print ('Arredondando para cima fica {}'.format(math.ceil(raiz)))
print ('Arredondando para baixo fica {}'.format(math.floor(raiz)))
# Gerando números aleatórios
num1 = random.random() #Gera numeros float entre 0 e 1 
num2 = random.randint(1 ,10) #Gera números inteiros de 1 a 10
print ('------------------------------------')
print(num1,"\n", num2)
print ('------------------------------------')
#Modúlo de emojis
print (emojis.encode('Dale bença :sunglasses:'))
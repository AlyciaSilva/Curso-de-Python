#Programa que diz se o número é impar ou par
import emojis
num = int(input('Digite um número inteiro para descobrir se é par ou impar: '))
if num % 2 == 0:
    print(emojis.encode('O número {} é par!! :heart::smile:'.format(num)))
else:
    print('O número {} é impar.'.format(num))
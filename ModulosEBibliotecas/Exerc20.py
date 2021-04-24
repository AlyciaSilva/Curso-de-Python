#Sortear de forma aleatória a ordem em que os grupos seram apresentados
import random, emojis
pNome = input('Insira o primeiro nome: ')
sNome = input('Insira o segundo nome: ')
tNome = input('Insira o terceiro nome: ')
qNome = input('Insira o quarto nome: ')
lista = [pNome, sNome, tNome, qNome]
random.shuffle (lista)
print ('A ordem de apresentação dos trabalhos é: {}'.format(lista))
print (emojis.encode('Boa sorte :grimacing::grimacing::grimacing:'))
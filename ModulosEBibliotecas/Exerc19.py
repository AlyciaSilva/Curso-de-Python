#Sorteio entre quatro alunos
import random, emojis
pNome = input('Insira o primeiro nome: ')
sNome = input('Insira o segundo nome: ')
tNome = input('Insira o terceiro nome: ')
qNome = input('Insira o quarto nome: ')
lista = [pNome, sNome, tNome, qNome]
sorteado = random.choice (lista)
print ('Dentre {}, {}, {} e {} \n O sorteado para limpar o quadro foi: {}'.format(pNome, sNome, tNome, qNome, sorteado))
print (emojis.encode('Boa sorte :grimacing::grimacing::grimacing:'))
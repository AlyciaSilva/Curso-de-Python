#Mudando cores/fonte e estilo no terminal
#style = 0- nenhum, 1-negrito, 4-sublinhado, 7-invertido 
#text = 30 ao 37 [branco,vermelho, verde, amarelo, azul, roxo, ciano e cinza]
#back = 40 ao 47 [mesmas cores a cima]
print('\033[1;31;43mOlá mundo!\033[m') #letra vermelha, em negrito com o fundo amarelo
#Com o \033[m no fim a cor da barra se extende até o ultimo caracter
#Usando o format
nome = Guanabara
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
cores{ 'limpa' : '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[33m',
    'pretoebranco' : '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))    
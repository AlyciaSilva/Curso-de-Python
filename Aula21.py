#Continuação sobre funções, aprendendo sobre Interactive Help, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
#Interactive help 
#help()#Também podendo ser usado direto no cmd
help(print) #Informa a funcionalidade de uma função

#Docstrings 
def contador (i,f,p):
    """
        -> faz uma contagem e mostra na tela
        :param i: incio da contagem 
        :param f: final da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end ='')
        c += p 
    print('FIM!')

contador(2, 10, 2)

help(contador)

#Parâmetros opcionais
def somar(a = 0,b = 0,c =0): #Todos os valores receberem 0
    s = a + b + c
    print(f'A soma vale {s}')

somar(8, 7) #Quando apenas forem passados uma quantidade menor de parâmetros não dará erro

#Com retorno
def somar(a = 0,b = 0,c =0):
    s = a + b + c
    return s

resultado = print(f'A soma vale {s}')
print(f'O resultado é {resultado}')
print(somar(8, 7)) 

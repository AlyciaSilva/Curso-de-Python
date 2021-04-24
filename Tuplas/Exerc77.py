#Exibir as vogais das palavras armazenadas nas tuplas
def separar (palavra):
    consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','ç')
    for i in range (0,21):
        print(palavra.strip(consoantes[i])) 
    return 0 
palavra = ('maça')
print (f' A palavra {palavra} tem as vogais: {separar(palavra)}')
print ('----------')
    #tam = len(separar.split())
    #for i2 in range (0,tam):
    #    if separar[i2] == 'a' or separar[i2] == 'e' or separar[i2] == 'i' or separar[i2] == 'o' or separar[i2] == 'u':        
    #        print(f'A palavra {palavra[i]} tem as vogais: {separar[i2]}')

#---------------------------------------------------------------------------------------------------------------------------
#def separar(palavra):
#    vogais = ('a', 'e', 'i', 'o', 'u')
#    v = ''
#    c = ''
#    for i in range(len(palavra)):
#        if palavra[i] == vogais[0] or palavra[i] == vogais[1] or palavra[i] == vogais[2] or palavra[i] == vogais[3] or palavra[i] == vogais[4]:
#            v += palavra[i]
#        else:
#            c += palavra[i]

#    print(f'vogais: {v}')
#    print(f'consoantes: {c}')    

#separar('lucas')


 #Lucas: (ok)
 
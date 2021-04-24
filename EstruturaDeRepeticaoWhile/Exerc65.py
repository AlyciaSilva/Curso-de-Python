#Programa para exibir menor e maior num e a média
media = 0
maior = 0
menor = 0
cont = 0
resp = ''
while resp != 'NÃO' and resp != 'NAO' and resp != 'N':
    num = int(input('Digite uma valor: '))
    media += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont +=1
    if cont == 1:
        menor = num
    resp = str(input('Deseja continuar? Digite Sim ou Não: ')).upper()
print('O maior número é {} e o menor {}, a média geral foi de {} com {} números'.format(maior, menor, media/cont, cont))        
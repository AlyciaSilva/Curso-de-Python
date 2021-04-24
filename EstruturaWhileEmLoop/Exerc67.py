#programa de tabuada
print('Digite um número negativo para parar a qualquer momento')
cont = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    while cont < 11: 
        print(f'{cont} X {valor} = {cont*valor}')
        cont += 1   
    if valor < 0:
        break
    print('---------------------------------') 
#Usando o while
n = 0
while n != 0:
    n = int(input('Digite um número:' ))
print('Fim')    
#
s = ''
while s == 'S':
    n = int(input('Digite um valor: '))
    s = str(input('Deseja contnua S para sim e N para não : '))
print("fim")
#
n3 = 0
par = impar = 0
while n3 != 0:
    n3 = int(input('Digite um valor: '))
    if n3 != 0:
        if n3 % 2 ==0:
            par += 1
        else:
            impar +=1    
print('VocÊ digitou {} numeros pares e {} impares'.format(par,impar))
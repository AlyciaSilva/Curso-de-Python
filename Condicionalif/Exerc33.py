#PRograma que lê 3 num e diz qual é o maior
print('Programa que diz quais dos 3 números é o maior e o menor')
n1 = int(input('Digite o primeiro num: '))
n2 = int(input('Agora o segundo: '))
n3 = int(input('E o terceiro: '))
if n1 > n2 and n1 > n3:
    print ('{} é o maior'.format(n1)) 
elif n2 > n1 and n2 > n3:
    print ('{} é o maior'.format(n2))     
else:
    print ('{} é o maior'.format(n3))    
if n1 < n2 and n1 < n3:
    print ('{} é o menor'.format(n1)) 
elif n2 < n1 and n2 < n3:
    print ('{} é o menor'.format(n2))     
else:
    print ('{} é o menor'.format(n3))    

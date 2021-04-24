#Montando uma PA com while
primeiroTermo = int(input('Informe o primeiro valor: '))
razao = int(input('Informe a razão: '))
print('Os primeiros valores são: ')
cont = 0
while cont < 11:
    print (primeiroTermo)
    primeiroTermo += razao
    cont += 1 
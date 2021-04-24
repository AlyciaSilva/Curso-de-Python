#Montando uma PA com while
primeiroTermo = int(input('Informe o primeiro valor: '))
razao = int(input('Informe a razão: '))
print('Os primeiros valores são: ')
cont = 0
limite = 5
while cont < limite:
    print (primeiroTermo)
    primeiroTermo += razao
    cont += 1
    if cont == 5:
        termos = int(input('Deseja informar mais termos? se sim quantos? Caso não, digite 0: '))
        if termos != 0:
            cont = 0
            limite = termos 
        
print('Fim.')
#Montando uma PA
primeiroTermo = int(input('Informe o primeiro valor: '))
razao = int(input('Informe a razão: '))
print('Os primeiros valores são: ')
for pa in range(primeiroTermo, primeiroTermo+20, razao):
    print(pa)
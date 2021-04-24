#Sequencia de fibonacci
quantidade = int(input('Digite a quantidade dos primeiro númeoros da sequência: '))
cont = 0
valorSec = 1
valorinicial = 0
while cont < quantidade:
    if cont == 0:
        print(valorinicial)
        print(valorSec)
    valorTerc = valorinicial + valorSec
    valorinicial = valorSec
    valorSec = valorTerc
    print(valorTerc)
    cont +=1    
print('FIM')
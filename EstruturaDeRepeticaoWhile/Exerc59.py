#Programa para calculos 
resp = 0
n1 = 0
n2 = 0
while resp != 5:
    n1 = int(input('Digite um  número: '))
    n2 = int(input('Digite outro: '))
    print('==========MENU==========')
    print('1-Somar')
    print('2-Multiplicar')
    print('3-Maior')
    print('4-Novos números')
    print('5-Sair do programa')
    print('========================')
    resp = int(input('Digite o valor: '))
    if resp > 6 or resp < 1:
        print('Número inválido')
    else:    
        if resp == 1:
            print('O resultado da soma é entre {} e {} é: {}'.format(n1, n2, n1+n2))
        elif resp == 2:
            print('O resultado da multiplicação entre {} e {} é: {}'.format(n1, n2, n1*n2))
        elif resp ==3:
            if n1 > n2:
                print('O maior número é {}'.format(n1))
            else:
                print('O maior número é {}'.format(n2))
print('Fim!')        
#programa que lê 41 valores e armazena numa tupla
print('Escreva quatro valores pra serem armazenado :slight_smile: ')
n1 = int(input('Digite o 1 valor: '))
n2 = int(input('Digite o 1 valor: '))
n3 = int(input('Digite o 1 valor: '))
n4 = int(input('Digite o 1 valor: '))
numeros = (n1,n2,n3,n4)
print(f'O número 9 apareceu {numeros.count(9)} vezes')
print(f'O número 3 apareceu pela primeia vez no {numeros.index(3)+1} lugar')
print('Os números pares foram: ')
cont = 0
for i in range(0,4):
    if numeros[i] % 2 == 0:
        print(numeros[i])
        cont += 1
if cont == 0:
    print('Não houve números impares!')
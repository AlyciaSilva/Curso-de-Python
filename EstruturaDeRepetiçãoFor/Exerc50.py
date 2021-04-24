#programa que leia número pares e faz soma
soma = 0
for somado in range(1,7):
    número = int(input('Informe um número: '))
    if número % 2 == 0:
        soma = soma + número
print('O resultado das somas é: {}'.format(soma))
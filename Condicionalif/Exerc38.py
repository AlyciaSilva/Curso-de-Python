#Programa de maior ou menos
print('Informe dois valores para saber qual é o maior')
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
if num1 > num2:
    print ('O número {} é maior!'.format(num1))
elif num1 < num2:
    print ('O número {} é maior!'.format(num2))
else:
    print('Não existe valor maior, ambos são iguais')
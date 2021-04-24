#Programa para verificar se o número é primo ou não
numero = int(input('Informe um número para descobrir se é primo ou não: '))
cont = 0
for num in range (1,numero+1):
    if numero % num == 0:
        cont = cont + 1 
if cont == 2:
    print('É um número primo')        
else:
    print('Não é')
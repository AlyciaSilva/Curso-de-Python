#Soma e contagem de número
cont = 0
print('Programa somador')
numero = 1
soma = 0
while numero != 999:
    numero = int(input('Digite um valor, para parar digite 999: '))
    if numero != 999:
        soma += numero
        cont += 1 
    else:
        print('FIM')
print('A soma total dos números foi {} e o total de número inseridos foi de {}'.format(soma,cont))           
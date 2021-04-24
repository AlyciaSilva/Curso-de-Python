#sete valores separdos em listas de impar e par
numeros = list()
impar = list()
par =  list()
valor = 0
for i in range(0,7):
    valor = int(input(f'Insira {i+1}º número: '))
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 != 0:
        impar.append(valor)    
par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(f'OS valores pares são: {par} \nE os impares: {impar}')
#Programa que lê vários números inteiros
print('Caso deseje parar digite 999')
num = ""
cont = 0 
soma = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if num == 999:
        cont -= 1
        soma -= 999
        break
print(f'O total de números fois {cont} e a soma foi: {soma}!!')    
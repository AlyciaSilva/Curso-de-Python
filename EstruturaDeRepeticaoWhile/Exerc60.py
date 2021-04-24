#Programa que mostra o fatorial de um  número
num = int(input('Insira um número para obter o fatorial: '))
fat = 1
while num > 1:
    fat = fat * num
    num = num - 1
print('O fatorial de {}! é {} '.format(num,fat))
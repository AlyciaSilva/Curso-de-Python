#Aula para while em looping
cont = 1
while cont <= 10:
    print(cont,' ', end = ' ')
    cont += 1
print('Acabou')
#Sem o looping infinito
n = s = 0
while n != 999 :
    n - int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))    
#Com loop
n = s = 0
while True:
    n - int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #Nova atualização do python (nova pep) com as f strings
idade = 37
nome = "José"
print(f'O {nome} tem {idade} anos') #python 3.6+
print('O {} tem {} anos'.format(nome,idade)) #python 3
print('O %s tem %d anos' %(nome,idade)) #python 2
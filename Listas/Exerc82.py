#Lista de impares e pares
lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Insira um número: ')))
    resp = str(input('Deseja parar (S/N)? ')).upper()
    if resp == 'S':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)
print('-'*30)
print(f'Os números que você digitou foram esses: {lista}')
print(f'Os pares são: {listaPar}')
print(f'E os impares: {listaImpar}')
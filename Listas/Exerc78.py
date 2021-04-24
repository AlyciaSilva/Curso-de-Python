#Mostrar qual foi o maior e o menor num em uma lista
maior = 0
menor = 0
lugarm = 0
lugarM = 0
lista = []
for posicao in range (0,5):
    lista.append(int(input(f'Digite um valor na posição {posicao}:')))
    if posicao == 0:
        menor = lista[posicao]
        maior = lista[posicao]
    elif lista[posicao] > maior:
        maior = lista[posicao]
        lugarM = posicao
    elif lista[posicao] < menor:
        menor = lista[posicao]    
        lugarm = posicao
print(f'O resultado da lista foi: {lista}')
print(f'O maior número foi {maior} na posição {lugarM}')
print(f'E o menor número foi {menor} na posição {lugarm}')
print('--------------------------------------')
#inserção de num na lista já na posição correta de inserção
lista = []
for cont in range(0,5):
    num = int(input('Insira os números: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        if num > lista[-1]:
            print(f'{num} foi adicionado na posição {lista[-1]}')
        else:
            print(f'{num} foi adicionado na posição {lista[0]}')    
    else:
        p = 0
        while p < len(lista):
            if num <= lista[p]:
                lista.insert(p,num)
                print(f'{num} foi adicionado na posição {lista[p]}')  
                break
            p += 1    
print(lista)
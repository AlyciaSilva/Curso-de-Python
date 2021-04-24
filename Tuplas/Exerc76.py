#Dados tabulados
print('--------------------------------------------------------')
print('Listagem de preços')
print('--------------------------------------------------------')
tabela = ('maçã', 2.22, 'uva', 2.50, 'pêra',5.55)
for lugar in range (0,len(tabela)):
    if lugar % 2 == 0:
        print(f'{tabela[lugar]:<10}', end ='')
    else: 
        print(f'{tabela[lugar]:>10}')
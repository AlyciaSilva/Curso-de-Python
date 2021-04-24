#matriz 3x3, com soma de pares digitados, soma da terceira coluna e o maior valor da segunda linha 
linha = list()
coluna = list()
somaPar = 0
somaTercColuna = 0
MaiorValor = 0
for lin in range(0,3):
    for col in range(0,3):
        coluna.append(int(input(f'Digite um valor para [{lin},{col}]:')))
    linha.append(coluna[:])
    coluna.clear()
print('='*30)
for lin in range(0,3):
    for col in range(0,3):
        if linha[lin][col] % 2 == 0:
            somaPar += linha[lin][col]
        if linha[1][col]:
            if linha[1][col] > MaiorValor:
                MaiorValor = linha[1][col]
        if col != 2:
            print(f' [ {linha[lin][col]} ] ', end=" ")
        else:
            print(f' [ {linha[lin][col]} ] ')
    if linha[lin][2]:
        somaTercColuna += linha[lin][2] 
#somaTercColuna = linha[0][2] + linha[1][2] + linha[2][2]
print(f'A soma de todos os valores pares digitados foram: {somaPar}')
print(f'A soma dos valores da terceira coluna foram: {somaTercColuna}')
print(f'E o maior valor da segunda linha é {MaiorValor}')
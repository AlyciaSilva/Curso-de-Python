#matriz 3x3
linha = list()
coluna = list()
for lin in range(0,3):
    for col in range(0,3):
        coluna.append(int(input(f'Digite um valor para [{lin},{col}]:')))
    linha.append(coluna[:])
    coluna.clear()
print('='*30)
for lin in range(0,3):
    for col in range(0,3):
        if col != 2:
            print(f' [ {linha[lin][col]} ] ', end=" ")
        else:
            print(f' [ {linha[lin][col]} ] ')
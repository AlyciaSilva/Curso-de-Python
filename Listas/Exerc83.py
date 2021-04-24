#Algoritmo que analisa se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Informe a sua extressão: '))
parenteses = []
for i in expressao:
    if i == '(':
        parenteses.append('(')
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
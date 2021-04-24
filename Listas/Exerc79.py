#cadastro de números em uma lista 
valores = []
organizado = []
print('Cadastro de números')
while True:
    valores.append(int(input('Digite um número: ')))
    for c, v in enumerate(valores):
        if valores.count(v) < 2:
            print('Valor adicionado com sucesso.')
            break
        else:
            print(f'Já existe o valor {v} então ele não será adicionado!')
            valores.pop(c)
            break
    resp = str(input('Deseja continuar? (S) para sim e (N) para não: ')).upper()
    if resp == 'N':
        break
print('=' * 30)
valores.sort()
print(f'Você digitou os valores: {valores}')
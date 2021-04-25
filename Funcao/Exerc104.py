def leiaInt (msg):
    """
    """
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            break
        else:
            print('ERRO! O VALOR INSERIDO NÃO É UM NÚMERO')
            break
    return num
print('-'*30)
n = leiaInt('Digite um número: ')    
print(f'O número digitado foi {n}')
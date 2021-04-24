def fatorial(number,show = False):
    """
        ->Função para relizar fatorial
        :param number: o número a calculado
        :param show: (opcional) mostra ou não a conta
        :return: o valor de fatorial de um number
    """
    result = 1
    if number == 0 or number == 1:
        result = 1
    else:
        for i in range (number, 0,-1):
            if show:
                if i == 1:
                    print(f'{i}= ', end='')
                else:    
                    print(f'{i} x ', end = '')
            result *= i
    return result
print('-'*30)
print(fatorial(5, True))
#programa para informar se um ano é bissexto ou não
ano = int(input('Infomw um ano: '))
if ano % 4 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))            
#Categoria de natação
idade = int(input('Insira a sua idade e verifique sua categoria de natação: '))
if idade <= 9:
    print('Categoria: Mirim')
elif idade >= 10 and idade <= 14:
    print('Infantil')
elif idade >= 15 and idade <= 19:
    print('Categoria: Junior')
elif idade == 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
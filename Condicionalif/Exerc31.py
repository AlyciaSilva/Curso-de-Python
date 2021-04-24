#programa que calcula o preço da passagem por km
km = int(input('Quantos km deseja percorrer? '))
if km <= 200:
    passagem = km * 0.50
    print('Sua passagem é de R${} '.format(passagem))
else:
    passagem = km * 0.45
    print('Sua passagem é de R${} '.format(passagem))
    

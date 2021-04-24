#Valor a ser pago por um produto
preco = float(input('Qual o preço do produto? R$'))
print('A vista em dinheiro/cheque, a vista no cartão, até 2x no cartão e 3x ou mais no cartão')
FormaDePagar = int(input('Escolha em ordem digitando um número de 1 a 4: '))
if FormaDePagar == 1:
    desconto = preco - (preco*10)/100
    print('O valor a pagar é de {}!!'.format(desconto))
elif FormaDePagar == 2:
    desconto = preco - (preco*5)/100
    print('O valor a pagar é de {}!!'.format(desconto))
elif FormaDePagar == 3:
    print('O valor a pagar é de {}!!'.format(preco))
elif FormaDePagar == 4:
    juros = preco + (preco*20)/100
    print('O valor a pagar é de {}!!'.format(juros))
else:
    print('Número inválido!!')
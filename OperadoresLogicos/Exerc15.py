#usando operadores aritméticos 
print ('Prohrma de aluguel de carros')
km = float (input('Quantos km você percorreu? '))
dias = int (input('Quantos dias você alugou? '))
valorDoCarro = dias * 60
kmRodados = km * 0.15
print ("O valor a ser pago é de R${:.2f}".format(valorDoCarro+kmRodados))
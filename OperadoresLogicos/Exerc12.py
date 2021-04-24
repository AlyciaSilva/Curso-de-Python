#usando operadores aritméticos 
print ('Digite o preço de seu produto e descubra o valor final com 5% de desconto')
valorP = float (input('Digite o valor do produto: '))
desconto = (5/100) * valorP
print ('O valor final é de {:.2f}'.format (valorP-desconto))

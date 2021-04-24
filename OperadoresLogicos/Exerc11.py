#usando operadores aritméticos 
print ('Descubra quanto de tinta vai precisar usar!')
altura = float (input('Digite o a altura da sua parede: '))
largura = float (input('Agora a largura: '))
area = altura * largura
print ('A área total é de {}, então serão necessários {} litros de tinta'.format(area, area/2))
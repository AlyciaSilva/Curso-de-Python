#Caixa eletrônico 
print('---------------CAIXA ELETRÔNICO-------------------')
valor = int(input('Digite o valor que deseja sacar: R$'))
moeda = valor
cont1 = 0 
cont2 = 0 
cont3 = 0
cont4 = 0
while True:
    if moeda >= 50:
        moeda -= 50
        cont1 += 1
    if moeda < 50:
        moeda -= 20
        cont2 += 1    
    if moeda < 20:
        moeda -= 10
        cont3 += 1
        break
while True:    
    if moeda < 10:
        moeda -= 1
        cont4 += 1
    if moeda == 0:
        break    
print(f"""O valor de saque foi R${valor} e a quantidade de cedulas a ser retiradas é de {cont1+cont2+cont3+cont4}
Sendo {cont1} de R$50
{cont2} de R$20
{cont3} de R$10
E {cont4} de R$1""")
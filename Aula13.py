for c in range(1,6): 
    print ('Oi')
print('FIM')    
#Para brintar o número de vezes que o usuário quer
n = int(input('Digite um valor: '))
for c2 in range(0,n+1):
    print(c2)
print('FIM')    
#Usando passos
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: ')) 
for c3 in range(i, f+1,p):
    print(c3)
print('FIM')  
#Pedindo valores para fazer somatórios
s = 0
for c4 in range(0,10):
    n = int(input('Digite um número: '))
    s = s + n
print('A soma de todos é {}'.format(s))    

#Aula do sistema de selação If 
nome = str(input('Qual o seu nome?')).strip()
if nome == 'Gustavo':
    print ('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')    
print('Bom dia {}'.format(nome))

#Media usando o if

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua media foi ruim! Estude mais!')    

#Estrturas condicionais alinhadas
nome =  str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print('Seu nome é bem popular no brasil')
elif nome in "Ana claúdia jéssica juliana":
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')    
print('Tenha um bom dia {}!!'.format(nome))
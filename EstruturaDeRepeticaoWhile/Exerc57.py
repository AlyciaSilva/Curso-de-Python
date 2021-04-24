#Exige que o usuário escreva correto
F = ''
M = ''
resp = ''
while resp != 'F' and resp != 'M':
    resp = str(input('Digite seu sexo, sendo F para feminino e M para masculino:')).upper()
    if resp != 'F' and resp != 'M':
        print('Carcter inválido, digite de novo.')
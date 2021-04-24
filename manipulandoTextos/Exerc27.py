#Exerciciopara mostrar o primeiro e ultimo nome de uma pessoa
nomecompleto = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é: ', nomecompleto[0])
print('Seu ultimo nome é: {}'.format(nomecompleto[len(nomecompleto)-1]))
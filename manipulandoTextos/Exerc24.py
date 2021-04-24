#Criar um programa que verifica o nome de uma cidade para ver se começa ou não com santos
cidade = input ('Digite o nome da sua cidade: ')
print ('A cidade possui o nome Santos no inicio? ')
teste = cidade.lower().split()
print ('santos' in teste[0])
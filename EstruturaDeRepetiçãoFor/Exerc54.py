#Programa para ler a idade e dizer quantas pessoas são maiores de idade
maiores = 0
menores = 0
for idade in range(1,8):
    DataDeNascimento = int(input('Digite a data de nascimento'))
    if 2020-DataDeNascimento < 21:
        menores = menores + 1
    elif 2020-DataDeNascimento >= 21:
        maiores = maiores + 1    
print ('Ao todo são {} maiores de idade e {} menores de idade!!'.format(maiores, menores))
#Programa para dizer a média de idade, quem  é o homem mais velho e quantas mulheres tem menos de 20
maior = 0
cont = 0
idadeS = 0
for grupo in range(0,4):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite seu sexo sendo (M) para masculino e (F) para femino: '))
    print('-----------------------------------')
    idadeS = idadeS + idade 
    if sexo == 'M' or 'm':
        if idade > maior:
            maior = idade
            nomeM = nome
    if sexo == 'F' or 'f':
        if idade < 20:
            cont = cont + 1
print('A media das idades é {}, {} é o homem com maior idade: {} e {} mulheres tem menos de 20 anos '.format(idadeS/4, nomeM, maior, cont))
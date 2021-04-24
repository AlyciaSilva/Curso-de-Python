#um programa que le nome, nascimento e carteira de trabalho e cadastre-o (com idade). Se a CTPS != 0, o dict receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
pessoa = dict()
ano = 0
while True:
    pessoa['nome'] = str(input('Seu nome: '))
    ano = int(input('Ano de nascimento: '))
    pessoa['ctps'] = int(input('Carteira de trabalho: 0 se n tiver '))
    pessoa['idade'] = datetime.now().year - ano         
    if pessoa['ctps'] == 0:
        print('=-'*30)
        for k, v in pessoa.items():
            print(f'-{k} tem o valor de {v}')
        break
    else:
        pessoa['contratações'] = int(input('Ano de contratação: '))
        pessoa['salário'] = int(input('Salário: R$'))
        pessoa['aposentadoria'] = pessoa['idade'] + (35 - (2020 - pessoa['contratações'])) 
        print('=-'*30)
        for k, v in pessoa.items():
            print(f'-{k} tem o valor de {v}')
        break
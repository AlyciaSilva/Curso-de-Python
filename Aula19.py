#Aula sobre dicionários em python
pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
pessoas ['peso'] = 98.5
#del pessoas['sexo'] <- apaga a chave e o valor em "sexo"
# pessoas['nome'] = 'Leandro' <- subistituiu o nome de "gustavo"  
for k, v in pessoas.items(): #items() mostra a chave e o valor correspondente a ela, para mostrar só o valor
#Se digita values e para só as chaves keys
    print(f'{k} = {v}')
print('**'*30)
#Criando dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print('--'*30)
#Como copiar um dicionário para por numa lista
estado = dict() #Outra forma de declarar dicionário
bras1l = list()
for c in range(0,3):
    estado['uf'] = str(input('Nome do estado: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Não é permitido o fatiamente "[:]" de dict para uma lista, ent se usa copy()
for e in brasil: #for para a lista
    for k,v in e.items(): #for para o dict
        print(f'o campo {k} tem  valor {v}.') 
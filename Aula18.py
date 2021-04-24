#Listas compostas
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
#criando uma lista dentro de uma lista
pessoas = list()
pessoas.append(dados[:])
pessoas = [['pedro',25],['maria',19],['joão',32]]
#printando por indices
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
#prática
print('-'*80)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Sem o [:] as listas criam conexão e não uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
galera = [['joão',19],['ana',37],['joaquim',13],['maria',45]] #outra forma de criar uma lista composta
print(galera)
for p in galera: #para exibir a lista
    #print(p[0]) #adicionando os índices se mostra apenas o que está naquele lugar
    print(f'{p[0]} tem {p[1]} anos')
    
#usando lista com inserção do usuário
galeras = list()
dados = list()
totalmaior = 0
totalmenor = 0
for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galeras.append(dados[:]) #fazendo da lista dados
    dados.clear() #limpando a lista clear
#print(galeras)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'temos {totalmaior} maiores e {totalmenor} menores de idade.')
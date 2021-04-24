#programa que lê peso e nomes guardando em lista
pesoNome = list()
pessoas = list()
maior = 0
menor = 0
cont = 0
while True:
    pesoNome.append(str(input('Insira seu nome: ')))
    pesoNome.append(float(input('Digite seu peso: ')))
    if cont == 0:
        menor = pesoNome[1]
    elif pesoNome[1] > maior:
        maior = pesoNome[1]
    elif pesoNome[1] < menor:
        menor = pesoNome[1]
    pessoas.append(pesoNome[:])
    pesoNome.clear()
    cont += 1
    resp = str(input('Deseja continuar? (s/n)')).lower()
    if resp == 'n':
        break
print(f'Foram cadastradas {cont} pessoas, o maior peso foi {maior}kg de: ', end = "") 
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}, ', end = "")
print(f' e o menor peso foi {menor}kg de: ')    
for p in pessoas:
    if p[1] == menor:
         print(f'{p[0]}, ', end = "")
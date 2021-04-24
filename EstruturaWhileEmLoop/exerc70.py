#simulador de caixa eletrônico 
caro = 0
precobarato = 0
cont = 0
soma = 0
while True:
    nomeProdutos = str(input('Digite o nome do produto: '))
    preco = float(input('Insira o preço: '))
    resp = str(input('Deseja continuar (S)sim ou não(N): ')).upper()
    if resp != 'S' and resp != 'N':
        print('Resposta inválida')
        break
    else:
        if cont == 0:
            precobarato = preco
        soma += preco
        if preco > 1000:
            caro += 1
        if precobarato > preco:
            precobarato = preco
            barato = nomeProdutos    
        cont += 1
        if resp == 'N':
            break
print(f'O somatório dos valores é {soma}, existem {caro} produto(s) custando mais de 1000 reais e o produto mais barato é {barato}, custando {precobarato}')
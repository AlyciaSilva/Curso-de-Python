#programa que lê vários num e coloca em ordem descrescente
num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? S para sim e N para não: ')).upper()
    if resp == 'N':
        break
print('-' * 30)
print(f'Você digitou {len(num)} elementos')
num.sort(reverse = True)
print(f'Em ordem decrescente são: {num}')
for i in range(0,len(num)):
    if 5 in num:
        print('Existe o número 5 nessa lista')
        break
    else:
        print('Não existe o número 5 nessa lista')
        break
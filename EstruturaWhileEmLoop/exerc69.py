#programa para ler finitas pessoas em um cadastro
print('Programa para ler idade e sexo de várias pessoas.')
maisDe18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Agora insira o seu sexo: F para feminino e M para masculino: ')).upper()
    resp = str(input('Deseja continuar? (S) sim (N) não: ')).upper()
    if resp != 'S' and resp != 'N':
        print('Resposta inválida')
        break
    else:
        if idade > 18:
            maisDe18 += 1
        if sexo == "M":
            homens += 1    
        if sexo == "F" and idade < 20:
            mulheres += 1 
        elif resp == "N":
            break
print(f'No total existem {maisDe18} pessoas maiores de 18, {homens} homen(s) e {mulheres} mulher(es) abaixo de 20 anos!')
#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = dict()
grupo = list()
media = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['idade'] = int(input('Idade:'))
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()
    while pessoa["sexo"] != 'F' and pessoa["sexo"] != 'M':
        print('Erro!! Insira apenas F ou M')
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()
    media += pessoa["idade"]
    grupo.append(pessoa.copy())
    resp = str(input('Deseja continuar?[S/N] ')).upper()
    while resp != 'S' and resp != 'N':
        print('Erro!! Insira apenas S ou N')
        resp = str(input('Deseja continuar?[S/N] ')).upper()
    if resp == 'N':
        break
print('=-'*30)
print(f'A) Ao todo nós temos {len(grupo)} pessoas cadastradas')
print(f'B) A média de idade é de {media/len(grupo):5.2f}')
print(f'C) As mulheres cadastradas foram: ', end = "")
for m in grupo:
    if m["sexo"] == 'F':
        print(f' {m["nome"]},', end = "")
print(' ')
print(f'D) Lista das pessoas que estão acima da média:')
for p in grupo:
    if p["idade"] > media/len(grupo):
        for k,v in p.items():
            print(f'    {k} = {v} ', end = "")
    print('')
print('<< ENCERRADO >>')
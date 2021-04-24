#Lista com nome e nota de alunos e exiba a média
nomenota = list()
alunos = list()
resp = ""
media = 0
numAluno = 0
n2 = 0
while resp != 'N':
    nomenota.append(str(input('Insira um nome: '))) 
    nomenota.append(float(input('Insira a 1° nota: ')))
    if nomenota[1] < 0 or nomenota[1]>10:
        while True:
            sub = float(input('Insira a 1° nota: '))
            if sub < 0 or sub>10:
                sub = float(input('Insira a 1° nota: '))
                if sub >= 0 or sub <= 10:
                    nomenota[1] = sub
                    break    
            else:
                nomenota[1] = sub
                break
    nomenota.append(float(input('Insira a 2° nota: ')))
    if nomenota[2] < 0 or nomenota[2]>10:
        while True:
            sub = float(input('Insira a 2° nota: '))
            if sub < 0 or sub>10:
                sub = float(input('Insira a 2° nota: '))
                if sub >= 0 or sub <= 10:
                    nomenota[2] = sub
                    break    
            else:
                nomenota[2] = sub
                break
    resp = str(input('Deseja inserir mais alunos? (S/N)')).upper()
    alunos.append(nomenota[:])
    nomenota.clear()
print('=-='*30)
print('Nº____Nome__________Média')
print('-'*30)
for x in range (0, len(alunos)):
        print(f'{x}º    ', end = "")
        print(f'{alunos[x][0]}          ', end = "")
        media = alunos[x][1] + alunos[x][2]
        print(f'{media/2}       ',)
print('-'*30)
while True:
    numAluno = int(input('Mostrar a nota de qual aluno? Insira seu número. Para parar digite (999)'))
    if numAluno != 999:
        for procura in range (0,len(alunos)): 
            if numAluno == procura:
                print(f'As nota de {alunos[procura][0]} foram {alunos[procura][1]} e {alunos[procura][2]}')
                print('-'*25)       
    else:
        break
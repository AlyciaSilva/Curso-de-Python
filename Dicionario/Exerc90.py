#Ler o nome e a nota de um aluno e infroma a situação dele 
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
print('=-'*30)
print(f'O nome é igual a {aluno["nome"]}')
print(f'A media é igual a {aluno["media"]}')
print(aluno["media"])
if aluno["media"] >= 6 and aluno["media"] <= 10 :
    print('A situação é APROVADO')
elif aluno["media"] >= 0 and aluno["media"] <= 5:
    print('A situação é REPROVADO')
else:
    print('Média inválida')
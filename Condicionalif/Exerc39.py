#Programa de alistamento
Nascimento = int(input('Informe seu ano de nascimento: '))
idade = 2020 - Nascimento
if idade < 18:
    falta = 18 - idade
    print ('Você ainda não tem a idade adequada, falta {} ano(s)'.format(falta))
elif idade == 18:
    print('Está na hora de se alistar!!!')    
else:
    print('Já passou da hora de se alistar')
    resposta = int(input('Você já se alistou? 1-Sim e 0-Não: '))
    if resposta == 1:
        print('Tudo certo!')
    elif resposta == 0:
        atraso = idade - 18
        print('Você está atrasado {} ano(s), resolva suas pendências'.format(atraso))
    else:
        print('Resposta inválida!!')
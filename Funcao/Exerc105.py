def notas(* num, sit = False):
    """
    -> função que analisa notas e a situação dos alunos
    :param num: uma ou mais notas (aceita várias)
    :param sit: (opcional), indica se a situação da turma
    :return: dicionário com resultados
    """
    maiorN = menorN = cont = media = 0
    geral = dict()
    for v in num:
        cont += 1
        if cont == 1:
            menorN = v
        if menorN > v:
            menorN = v
        if v > maiorN:
            maiorN = v
        media += v    
    geral['total'] = cont
    geral['maior'] = maiorN
    geral['menor'] = menorN
    geral['media'] = media/cont
    if sit:
        if media/cont < 6:
            geral['situacao'] = 'RUIM'
        if media/cont >= 6 and media/cont < 7:
            geral['situacao'] = 'RAZOAVEL'
        if media/cont > 6:
            geral['situacao'] = 'BOA'    
    return geral    
print(notas(2.5, 5.5, 8.0, sit = True))    
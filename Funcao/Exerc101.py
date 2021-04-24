def voto(year):
    """
        ->Função para relizar a verificação de voto
        :param year: o número de nascimento
        :return: o resultado do status
    """
    yearsOld = 2020 - year
    if yearsOld >= 18 and yearsOld < 66:
        result = "Voto Obrigatório"
    elif yearsOld > 65 or yearsOld >= 16 and yearsOld < 18:
        result = "Voto Opcional"
    else:
        result = "Voto Negado"
    return result
def tracos ():
    print('-'*30)

tracos()
birthYear = int(input('Que ano você nasceu? '))
print(f'Com {2020 - birthYear} anos: {voto(birthYear)}')
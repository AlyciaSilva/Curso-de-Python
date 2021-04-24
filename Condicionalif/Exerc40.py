#PRograma de média 
print('Insira suas notas para saber sua situação')
Nota1 = float(input('Insira Sua primeira nota: '))
if Nota1 > 10 or Nota1 < 0:
    print('Nota inválida')    
else:
    Nota2 = float(input('Agora a segunda: '))
    if Nota2 > 10 or Nota2 < 0:
        print('Nota inválida')    
    else:
        media = (Nota1+Nota2)/2
        if media < 5:
            print('Você foi reprovado!!')
        elif media > 5 and media <= 6.9:
            print('Você está na recupperação!')
        elif media >= 7:
            print('Você foi aprovado!!!')
#Aula sobre módulos e pacotes
import Aula22Uteis
# ou from Aula22Uteis impport fatoial,dobro (não é tão recomendado por poder causar problemas)
num = int(input('Digite um valor: '))
fat = Aula22Uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Aula22Uteis.dobro(num)}')
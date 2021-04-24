#Programa que diz  se há como existir um triangulo
print('Digite 3 valores para construir um triângulo')
a = float(input('Medida do lado um: '))
b = float(input('Medida do lado dois: '))
c = float(input('Medida do lado três: '))
if b - c < a < b + c and a - c < b < a + c and b - a < c < b + a:
    print('Parabéns!! É um triângulo ')
else:
    print('Não é um triângulo :( ')    
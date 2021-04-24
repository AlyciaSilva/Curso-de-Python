#Aula sobre funções
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma de A+B é {s}')

#programa principal
soma(b=4, a=5)
soma(7,2)

#empacotamento de dados

def contador(* num):
    for valor in num:
        print(valor, end = "")
    print('Fim!!')
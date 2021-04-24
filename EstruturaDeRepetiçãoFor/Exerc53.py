#Exercicio para dizer se a frase é ou não um palindromo
frase = str(input('Digite uma frase e descubra se é um palindrono: ')).strip().lower()
letras = frase.split()
juntos = ''.join(letras)
inverso = ''
for letra in range (len(juntos) - 1, -1, -1):
    inverso += juntos[letra]
print(juntos, inverso)    
if juntos == inverso:
    print('É um palindromo')
else:
    print('Não é um palindromo')

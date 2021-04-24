#Programa para tirar o IMC de alguém
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Você está abaixo do peso!!')
elif imc >= 18.5 or imc <= 25:
    print('Você está no peso ideal!!!')
elif imc > 25 or imc <= 30:
    print('Você está com sobrepeso.')    
elif imc > 30 or imc <= 40:
    print('Você está obeso.')
else:
    print('Você possui obesidade morbida.')
#Calcula o aumento que o salário do funcionário vai sofrer
salario = float(input('Digite seu salário: R$'))
if salario >= 1200.00:
    aumento = (0.10 * salario) + salario
    print('Seu salário agora é de R${}'.format(aumento))
else:
    aumento = (0.15 * salario) + salario
    print('Seu salário agora é de R${}'.format(aumento))
    
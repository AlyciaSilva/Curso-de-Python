#Tabuada
num = int(input('Digite o número que você deseja saber a tabuada: '))
print('A tabuada de {} é: '.format(num))
for tabuada in range(0,11):
    print('{}X{}={}'.format(num, tabuada, num*tabuada))

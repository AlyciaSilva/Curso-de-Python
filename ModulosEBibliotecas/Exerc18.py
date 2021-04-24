#Valores de seno, cosseno e tangente de um ângulo
import math, emojis
angulo = int (input('Informe um ângulo para ser mostrado o sen, cos e a tangente: '))
print('O ângulo {}°, tem como sen: {:.2f} \n cos: {:.2f} e tang: {:.2f}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))
print(emojis.encode(':smile:'))
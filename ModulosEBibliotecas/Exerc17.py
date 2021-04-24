#Calculo da hipotenusa
import math
catetoOposto = float(input('Insira o cateto oposto: '))
catetoAdjacente = float(input('Insira o cateto adjacente: '))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print('A hipotenusa é {}'.format(hipotenusa))
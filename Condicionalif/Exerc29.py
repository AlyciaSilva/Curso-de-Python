#Programa para dar multas
import emojis
km = int(input('Quantos quilometros você percorreu? '))
if km > 80:
    print(emojis.encode('Você está sendo multado :angry::cop:'))
    multa = (km - 80) * 7
    print(emojis.encode('O valor da sua multa é de R${} :moneybag::moneybag:'.format(multa)))
else:
    print(emojis.encode8('Parabéns, você estava dentro do limite de velocidade!!! :smile::smile::cop:'))    
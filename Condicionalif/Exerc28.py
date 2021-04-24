#Um número aleatório é gerado e o usuário deve inserir um número para descobrir se acertou
import random, emojis
num = random.randint (0 ,5)
numusuario = int(input('Digite um número inteiro de 0 a 5 e tente acertar se foi o mesmo que o computador: '))
if num == numusuario:
    print(emojis.encode('Parabéns :open_mouth::open_mouth:!! \nVocê é algum tipo de bruxo(a)?'))
else:
    print(emojis.encode('Parace que não foi dessa vez :sunglasses: :stuck_out_tongue_winking_eye:'))
    print('O número foi {}, boa sorte na próxima!!!'.format(num))
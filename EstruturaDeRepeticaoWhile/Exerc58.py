#Um número aleatório é gerado e o usuário deve inserir um número para descobrir se acertou
import random, emojis
cont = 0
numusuario = 0
num = random.randint (0 ,10)
while numusuario != num:  
    numusuario = int(input('Digite um número inteiro de 0 a 10 e tente acertar se foi o mesmo que o computador: '))
    if numusuario != num:
         print(emojis.encode('Parace que não foi dessa vez, va tentando ai meu chapa :sunglasses: :stuck_out_tongue_winking_eye:'))
    cont +=1   
if cont == 1:
     print(emojis.encode('Parabéns :open_mouth::open_mouth:!! \nVocê é algum tipo de bruxo(a)?'))
     print('O número foi de tentativas foi {}, UAU!!!'.format(cont))
else:
    print('Finalmente!!! o número de tentaivas até o acerto foi de: {} vezes'.format(cont))
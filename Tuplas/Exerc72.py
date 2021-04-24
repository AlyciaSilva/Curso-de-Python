#número que lê de 0 a 20
extenso = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte']
print('leitor de números de 0 a 20')
print('********************************')
while True:
    numero = int(input('Digite um número para ser escrito por extenso: '))
    if numero <= 20 and numero >= 0:
        print(f'O número {numero} por extenso é: {extenso[numero]}!')
        break
    print('Número inválido! Informe novamente')

#conversão para binário, octal ou hexadecimal
número = int(input('Digite um número para conversão: '))
print('Agora escolha sua conversão')
escolha = int(input('Digite (1) para binário \n (2) para octal \n e (3) para hexadecimal: '))
if escolha == 1:
    print(' {} convertido para binário é: {}'.format(escolha,bin(escolha)))
elif escolha == 2:
    print(' {} convertido para octal é: {}'.format(escolha,oct(escolha)))
elif escolha == 3:
    print(' {} convertido para hexadecimal é: {}'.format(escolha,hex(escolha)))
else:
    print('Número inválido')
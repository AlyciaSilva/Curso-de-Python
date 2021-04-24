#Pega um nome e coloca-lo em letras grandes, pequenas a contagemde todas as letras e apenas a do primeiro nome
nome = str(input('Digite o seu nome:')).strip
print('\nEsse é o seu nome com todas as letras grandes {}'.format(nome.upper()))
print('\n E esse é o seu nome agora em minusculo {}'.format(nome.lower()))
print('\n Ao todo existem {} letras'.format(len(nome) - nome.count(' '))
print('Seu primeiro nome  tem {} letras'.format(nome.find(' '))

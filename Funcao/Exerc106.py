def ajuda(msg):
    """"
    -> Guia nas funções e libs
    :param msg: palavra chave de busca
    :return: A resposta da busca  
    """
    help(msg)

print('-'*30)
while True:
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        print('-'*20)
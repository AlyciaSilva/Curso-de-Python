#
palavras = ('casa','passado')
for p in palavras:
    print(f'Na palavra {p.upper()} tem as vogais ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = '') 











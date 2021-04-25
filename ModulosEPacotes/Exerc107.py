from Exerc107P import moeda

p = float(input("Escreva o preço: "))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro é {moeda.dobro(p)}')
print(f'o aumento com 10% é {moeda.aumentar(p,10)}')
print(f'a diminuição com 13% é de {moeda.diminuir(p,13)}')
from Exerc107P import moeda

p = float(input("Escreva o preço: "))
print(f'a metade de {p} é {moeda.moeda(moeda.metade(p))}') 
print(f'o dobro é {moeda.moeda(moeda.dobro(p))}') 
print(f'o aumento com 10% é {moeda.moeda(moeda.aumentar(p,10))}') 
print(f'a diminuição com 13% é de {moeda.moeda(moeda.diminuir(p,13))}')
#Programa para ler peso maior e menor
maior = 0
menor = 0
for peso in range(1,6):
    pesoPessoas = float(input('Digite o peso: '))
    if peso == 1:
        menor = pesoPessoas
    if pesoPessoas > maior:
        maior = pesoPessoas
    elif pesoPessoas < menor:
        menor = pesoPessoas
print('O maior peso foi {} e o menor {}!'.format(maior,menor))      
#soma de números impares multiplos de 3
soma = 0
for impares in range(0,501,3):
    if impares % 2 != 0:
        soma = soma + impares
print(soma)
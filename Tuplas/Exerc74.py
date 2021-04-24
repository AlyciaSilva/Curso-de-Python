#gerador de números aleatórios em uma tupla
import random
n1 = random.randint(0,9999)
n2 = random.randint(0,9999)
n3 = random.randint(0,9999)
n4 = random.randint(0,9999)
n5 = random.randint(0,9999)
menor = 0
maior = 0
num = (n1,n2,n3,n4,n5)
for i in range (0,5):
    if i == 0:
        menor = num[i]
    elif maior < num[i]:
        maior = num[i]
    elif menor > num[i]:
        menor = num[i]    
print(f'Os números sorteados foram: {num}')
print(f'O maior número foi {maior}')
print(f'E o menor {menor}')
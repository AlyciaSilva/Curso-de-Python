#Aula sobre listas
num = [2,5,9,4,1]
num[2] = 3 #faz a posção2 receber o num 3
num.append(7) #adiciona o valor 7 a lista
num.sort(reverse = True) #organiza os números, porém quando o reverso está verdaddeiro coloca de forma decrescente
num.insert(2,0) # na posição 2 o num 0 será inserido
num.pop(2) # exclui o número na posição 2, caso não seja passado um parâmetro o primeiro valor será excluído
num.remove(4) #Remove o valor que estiver passado por parâmetro 
print(num)
print(f'essa lista tem {len(num)} elementos')
# adicionando valores a uma lista
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista!')
#Diferença de ligação para cópia
a = [1,2,3,4]
b = a #Com o acrescimo de [:] depois do 'a', deixa de se tornar uma ligação e vira uma cópia
b[2] = 8
print(f'lista a: {a}')
print(f'Lista b: {b}')
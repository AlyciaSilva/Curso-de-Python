#Aula sobre tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
#print(lanche[1])
#print(lanche[1:3])
#print(lanche[-1])
#tuplas são imutavéis 
#for comida in lanche:
#    print(f'Vou comer {comida}')
#for  pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')
#for count in range (0,len(lanche)):
#    print(f'Eu vou comer {lanche[count]} na posição {count}')
#print('Comi pra caramba')
print(sorted(lanche)) #coloca em ordem alfabética
# "soma" de tuplas
a = (2,5,4)
b = (5,8,1,2)
c = b+a
print(len(c))
print(c.count(5)) #encontra quantas vzs aparece o num 5 aparece
print(c.index(8)) #informa em que index o 8 está
#como deletar uma tupla
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #Deleta toda a tupla, não podendo selecionar apenas um dado para apagar, sempre sendo a tupla toda
print(pessoa)
#Fatia pegando a letra que corresponde ao número
frase = 'Curso em Video Python'
print (frase[3])
#Fatia pegando de X número até X número
print (frase[3:13])
#Fatia pegando de X número até X número e pulando x vezes
print (frase [3:13:2])
#Escreve um texto longo sem a necessidade de colocar vários prints
print("""O Mestre na arte da vida faz pouca distinção entre o seu trabalho e o seu lazer, 
entre a sua mente e o seu corpo, entre a sua educação e a sua recreação, entre o seu amor e a sua religião. 
 dificilmente sabe distinguir um corpo do outro. Ele simplesmente persegue sua visão de excelência em tudo que faz, 
 deixando para os outros a decisão de saber se está trabalhando ou se divertindo. Ele acha que está sempre fazendo as
  duas coisas simultaneamente.""")
#Conta o núemro de vezes o número de letras aparece, podendo juntar com outros métodos, colocando 'o' dentro do método 
#count ele conta a quantidades de O's depois da alteração do upper
print(frase.upper().count('O'))
#o len faz a contagem de quantos caracteres tem e o stripp retira os espaços denecessários
print(len(frase.strip()))
#replace troca as palavras, só sera salvo se a variavel receber o resultado
print(frase.replace('Python', 'Android'))
#Verifica se a palavra está na frase, usando o find ele mostra a posição da palavra
print('Curso' in frase)
print(frase.find('Curso'))
#o slipt separa a frase
print (frase.split())
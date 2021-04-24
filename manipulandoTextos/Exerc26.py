#Descobrir quantos 'A's tem na frase e a primeira e a ultima vez que ela apareceu
frase = str(input ('Digite a sua frase: ')).strip()
print('A letra A aparece na frase ',frase.upper().count('A'),'vezes')
print('O primeiro A está no ', frase.upper().find('A') + 1,' lugar')
print('E o ultimo A está no', frase.upper().rfind('A') + 1, 'lugar')
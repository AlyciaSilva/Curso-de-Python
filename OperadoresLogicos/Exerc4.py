#Usando tipos primitivos e as informações sobre o valor
x = input ('Agora digite algo e vamos descobrir qual o seu tipo mais informaçãoes sobre: ')
print (type(x))
print ('É númerico? ', x.isnumeric())
print ('É uma letra?', x.isalpha())
print ('É um número?', x.isalnum())
print ('É ascii?', x.isascii())
print('É decimal?', x.isdecimal())
print('É um digito?', x.isdigit())
print ('É um identificador?', x.isidentifier())
print ('Está minusculo?', x.islower())
print ('Pode ser impresso?', x.isprintable())
print ('É um espaço?', x.isspace())
print('Está capitalizada?', x.istitle())
print('Está todo maisculo?', x.isupper())
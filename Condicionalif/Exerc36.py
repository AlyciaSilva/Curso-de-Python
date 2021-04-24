#Programa para financiar uma casa
print('---Programa de emprestimo bancário---')
ValorDaCasa = float(input('Qual o valor da casa? '))
SalarioDoComprador = float(input('Qual o seu salário: '))
AnosPagamento = int(input('Em quantos anos pretende pagar? '))
OsPorcentos = (30*SalarioDoComprador)/100
PrestacaoMensal = ValorDaCasa/(AnosPagamento * 12)
if OsPorcentos < PrestacaoMensal:
    print('Você não pode financiar essa casa, porquê excedeu o limite de 30% do seu salário')
elif OsPorcentos > PrestacaoMensal:     
    print('Em {} anos você tera que pagar mensalmente {:200.2f}!'.format(AnosPagamento, PrestacaoMensal))
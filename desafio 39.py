from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
tempo = atual - (ano+18)
saldo = 18 - idade
alist = ano + 18
print('Quem nasceu em {} tem {} anos.'.format(ano,idade))
if idade == 18:
    print('Você ja tem {}, tem que se alistar ainda este ano'.format(idade))
elif idade > 18:
    print('Você tem {} anos, ja deveria ter se alistado há {} anos atrás. Você deveria ter se alistado em {}.'.format(idade,tempo,alist))
else:
    print('Você ainda não tem 18 anos, vai precisar se alistar só daqui a {} anos.Você vai ser alistar em {}.'.format(saldo,alist))
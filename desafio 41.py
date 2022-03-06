from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta '))
ano = date.today().year
idade = ano - nasc

if idade <=9:
    print('o atleta tem {} anos e é classificado como MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é classificado como INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é classificado como JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é classificado como MASTER.'.format(idade))
else:
    print('O atleta tem {} anos e é classificado como MASTER.'.format(idade))
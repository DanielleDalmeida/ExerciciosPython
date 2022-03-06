n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))

m = (n1 + n2)/2

if m < 5:
    print('Sua média foi {:.2f}, você esta reprovado'.format(m))
elif m == 5 or m >= 6.9:
    print('Sua média foi {:.2f}, você esta de recuperação.'.format(m))
else:
    print('Sua média foi {:.2f}, você está aprovado.'.format(m))
peso = float(input('Qual o seu peso: '))
alt = float(input('Qual a sua alturqa: '))
imc = peso / (alt*alt)
if imc < 18.5:
    print('Abaixo do peso. Seu imc é {:.2f}.'.format(imc)
elif imc <=24.9:
    print('Peso normal. Seu imc é {:.2f}.'.format(imc))
elif imc <= 29.9:
    print('Sobrepeso. Seu imc é {:.2f}.'.format(imc))
elif imc <= 34.9:
    print('Obesidade Grau 1. Seu imc é {:.2f}.'.format(imc))
elif imc <=39.9:
    print ('Obesidade Grau 2. Seu imc é {:.2f}.'.format(imc))
else:
    print('Obesidade Grau 3 ou Mórbida. Seu imc é {:.2f}.'.format(imc))
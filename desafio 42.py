n1 = float(input('Digite o lado número 1 do triangulo: '))
n2 = float(input('Digite o lado número 2 do triangulo: '))
n3 = float(input('Digite o lado número 3 do triangulo: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os lados formam um triângulo.')
    if n1 == n2 == n3:
        print('Equilatero')
    if n1 != n2 != n3:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Os lados não formam um triângulo')
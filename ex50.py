a = 0
for x in range (1,7):
    x = int(input('Digite um número inteiro: '))
    if x % 2 ==0:
        a = a + x
print("A soma dos pares é {}".format(a))

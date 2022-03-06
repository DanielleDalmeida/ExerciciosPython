from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1,8):
    i = int(input("Em que ano a {}° nasceu? ".format(p)))
    idade = atual - i
    if idade >=21:
        print("A pessoa é maior")
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} maiores de idade".format(totmaior))
print("Ao todo tivemos {} menores de idade".format(totmenor))
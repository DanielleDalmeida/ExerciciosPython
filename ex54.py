frase = str(input('Digite a palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print("O Inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palimetro")
else:
    print("não é palimetro")

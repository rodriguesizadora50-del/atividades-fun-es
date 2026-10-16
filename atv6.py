def maior_numero(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    return maior


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

resultado = maior_numero(a, b, c)

print("O maior número é:", resultado)
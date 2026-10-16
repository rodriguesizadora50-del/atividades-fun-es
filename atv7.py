def contar_pares(numeros):
    quantidade = 0

    for numero in numeros:
        if numero % 2 == 0:
            quantidade = quantidade + 1

    return quantidade


numeros = [12, 7, 9, 20, 14, 3, 8, 11]

resultado = contar_pares(numeros)

print("Quantidade de números pares:", resultado)
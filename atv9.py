def contar_acima_do_valor(precos, limite):
    quantidade = 0

    for preco in precos:
        if preco > limite:
            quantidade = quantidade + 1

    return quantidade


precos = [10, 25, 80, 15, 120, 45]

limite = float(input("Digite o limite de preço: R$ "))

resultado = contar_acima_do_valor(precos, limite)

print("Quantidade de produtos acima do limite:", resultado)
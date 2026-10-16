def contar_sem_estoque(estoque):
    quantidade = 0

    for item in estoque:
        if item == 0:
            quantidade = quantidade + 1

    return quantidade


def contar_estoque_baixo(estoque):
    quantidade = 0

    for item in estoque:
        if item > 0 and item < 5:
            quantidade = quantidade + 1

    return quantidade


def maior_estoque(estoque):
    maior = estoque[0]

    for item in estoque:
        if item > maior:
            maior = item

    return maior


estoque = [15, 2, 8, 0, 20, 4, 11]

sem_estoque = contar_sem_estoque(estoque)
estoque_baixo = contar_estoque_baixo(estoque)
maior = maior_estoque(estoque)

print("RELATÓRIO DE ESTOQUE")
print("Itens sem estoque:", sem_estoque)
print("Itens com estoque baixo:", estoque_baixo)
print("Maior quantidade em estoque:", maior)
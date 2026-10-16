def calcular_desconto(preco, desconto):
    valor_desconto = preco * desconto / 100
    return preco - valor_desconto


preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

resultado = calcular_desconto(preco, desconto)

print("Preço final: R$", round(resultado, 2))
def converter_minutos(horas):
    return horas * 60


horas = float(input("Digite a quantidade de horas: "))

resultado = converter_minutos(horas)

print("Total de minutos:", resultado)
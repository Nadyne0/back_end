peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    print("O IMC é: %.2f" % imc)


calcular_imc(peso, altura)

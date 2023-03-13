# Cálculo de IMC
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Código do IMC
imc = peso / altura ** 2

# Mostrar o resultado no terminal
print("Seu IMC é:", round(imc, 2))

try:
    peso = float(input("digite o seu peso em kg (ex.: 70.5): "))
    altura = float(input("digite a sua altura em metros (ex.: 1.75): "))

    imc = peso / (altura ** 2)

    print("\n--- Resultado---")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso normal")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")

    print(f"Seu IMC é: {imc:.2f}")

except ValueError:
    print("\n[Erro] Você digitou uma letra ou usou vírgula! Por favor, use apenas números e ponto.")
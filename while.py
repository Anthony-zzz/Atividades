soma = 0
while True:
    numero = float(input("Digite um número: "))
    soma += numero
    if numero == 0:
        break
print(f"A soma total dos números digitados é: {soma}")
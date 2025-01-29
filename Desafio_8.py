while True:
    try:
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
        if 1 <= numero <= 10:
            break
        else:
            print("Por favor, insira um número entre 1 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

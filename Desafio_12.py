lista = []

for i in range(10):
    valor = int(input(f'Digite o valor para a posição {i}: '))
    lista.append(valor)

impares = []
for valor in lista:
    if valor % 2 != 0:
        impares.append(valor)

print(f'A lista digitada foi: {lista}')
print(f'A lista contém {len(impares)} números impares. São eles {impares}')
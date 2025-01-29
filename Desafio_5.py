print('Parabéns, você fechou uma venda!')
nome = input('Informe o nome do imóvel:')
valor = float(input('Informe o valor do imóvel: '))

if valor >= 50000:
    comissao = valor * 0.20
elif valor >= 30000:
    comissao = valor * 0.15
else:
    comissao = valor * 0.10

print("\n--- Resultado ---")
print(f"Nome do imóvel: {nome}")
print(f"Valor do imóvel: R$ {valor:.2f}")
print(f"Comissão: R$ {comissao:.2f}")
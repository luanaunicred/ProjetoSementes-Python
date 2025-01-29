print("Olá, vamos registrar seus produtos!")

produto = input("Informe o nome do produto: ")
preco = float(input('Informe o valor do produto:'))
quantidade = int(input('Informe a quantidade:'))

valor_final = preco * quantidade
desconto10 = ( valor_final * 10 ) / 100
desconto20 = ( valor_final * 20 ) / 100
desconto25 = ( valor_final * 25 ) / 100


if quantidade <= 10:
    print("O valor total: R$ {}".format(valor_final))
elif 11 <= quantidade <= 20:
    valor_final = (valor_final - desconto10)
    print(f"O valor final calculado com 10% de desconto, foi de: R$ {valor_final:.2f}")
elif 21 <= quantidade <= 50:
    valor_final = (valor_final - desconto20)
    print(f"O valor final calculado com 20% de desconto, foi de: R$ {valor_final:.2f}")
else:
    valor_final = (valor_final - desconto25)
    print(f"O valor final calculado com 25% de desconto, foi de: R$ {valor_final:.2f}")
print("Bem-vindo à calculadora básica!")

print('Insira os valores a serem calculados e depois escolha o tipo de operação desejada.')

valor1 = float(input('Insira o primeiro valor:'))
valor2 = float(input('Insira o segundo valor: '))

opcao = input('Selecione a opção desejada, digitando 1-ADIÇÃO, 2-SUBTRAÇÃO, 3-MULTIPLICAÇÃO ou 4-DIVISÃO:')

match opcao:
    case '1':
        print("1 - Adição (+)")
        resultado = valor1 + valor2
        print('O resultado é {}'.format(resultado))
    case '2':
        print("2 - Subtração (-)")
        resultado = valor1 - valor2
        print('O resultado é {}'.format(resultado))
    case '3':
        print("3 - Multiplicação (*)")
        resultado = valor1 * valor2
        print('O resultado é {}'.format(resultado))
    case '4':
        print("4 - Divisão (/)")
        resultado = valor1 / valor2
        print('O resultado é {}'.format(resultado))
    case _:
        print('Opção inválida')
print('Vamos brincar de dividir! A seguir você vai informar 2 números que serão divididos. Não informe zero no segundo valor!')

numero1 = float(input('Informe o primeiro valor: '))
numero2 = float(input('Informe o segundo valor: '))

while numero2 == 0:
    print('ATENÇÃO!! O segundo número precisa ser diferente de zero.')
    numero2 = float(input('Informe um número diferente de zero: '))

divisao = numero1 / numero2

print(f'O resultado da divisão de {numero1} e {numero2} é: {divisao:.2f}.')
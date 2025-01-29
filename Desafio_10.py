def mostralinha():
    print('-' * 50)

mostralinha()
print('BEM VINDO AO SISTEMA DE ALUNOS')
mostralinha()

def media_aluno():

    while True:
        nome = input('Informe o nome do aluno: ')

        nota1 = float(input('Informe a nota do primeiro semestre: '))
        nota2 = float(input('Informe a nota do segundo semestre: '))

        media = ((nota1 + nota2) / 2)

        if media >= 7:
            print(f'A média final de {nome} foi {media:.2f}. Você está aprovado! ')
        else:
            print(f'Infelizmente a média final de {nome} foi {media}. Você está reprovado! Estude mais ano que vem!!!')

        opcao = input('Deseja calcular a média de outro aluno? (s/n): ').strip().lower()
        if opcao == 'n':
            print('Encerrando o programa. Muito obrigada e até a próxima!')
            break

media_aluno()
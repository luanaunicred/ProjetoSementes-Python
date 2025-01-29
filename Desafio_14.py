nomes = ['Luana', 'Diogo', 'Ceci', 'Marley', 'Mel', 'Nelson', 'Nair', 'Elaine', 'Jorge', 'Rita',
                'Vania', 'Fernando', 'Luana', 'Nair', 'Claudio', 'Claudinho', 'Luana', 'Jorge','Nelson', 'Nelson']

print('Lista completa de nomes: ')
print(nomes)

print('\nOs nomes repetidos serão excluídos agora...')

repetidos = []

for nome in nomes:
    if nome not in repetidos:
        repetidos.append(nome)

print('\nSegue a lista após exclusão dos nomes repetidos! ')
print(repetidos)
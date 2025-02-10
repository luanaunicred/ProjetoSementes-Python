def pesquisa_nome():

    lista_nomes = []

    for i in range(10):
        nome = input(f'Digite o {i+1}° nome: ')
        lista_nomes.append(nome.lower())

    pesquisa = input('Informe o nome que deseja pesquisar na lista: ')
    pesquisa = pesquisa.lower()

    if pesquisa in lista_nomes:
        print('Achei :)')
    else:
        print('Não achei. :/')

pesquisa_nome()

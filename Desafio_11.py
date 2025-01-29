usuario_certo = "aluno"
senha_certa = "segredo"

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if usuario == usuario_certo and senha == senha_certa:
        print("Seja Bem vindo! Seu Login foi efetuado com sucesso.")
        break
    else:
        tentativas = tentativas + 1
        print("Usuário ou senha incorretos. Após 3 tentativas sem sucesso você será bloqueado.")

        if tentativas == max_tentativas:
            print("Conta bloqueada. Número máximo de tentativas foi excedido.")
        else:
            print(f"Tentativas restantes: {max_tentativas - tentativas}")
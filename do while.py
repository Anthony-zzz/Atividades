login_correto = "admin"
senha_correta = "1234"
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("Acesso permitido!")
        break  
    else:
        print("Login ou senha incorretos. Tente novamente.\n")
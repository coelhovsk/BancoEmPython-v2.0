from time import sleep


def buscar_usuario(cpf):
    """
    Essa função busca o CPF do usuário em users.txt
    e retorna o valor True se o CPF ja estiver cadastrado.
    """
    with open('users.txt', 'r') as arquivo:
        if cpf in arquivo.read():
            print(45 * '\033[30m-=')
            print(
                '\033[31mO CPF escrito já está cadastrado, faça login, verifique seu CPF ou selecione outra '
                'opção.\033[m')
            print(45 * '\033[30m-=\033[m')
            sleep(1.5)
            from main import menu
            menu()
            return True
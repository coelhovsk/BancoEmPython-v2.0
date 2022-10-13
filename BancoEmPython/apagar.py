from time import sleep
base = dict()


def apagar_cliente():
    """
    """
    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        print('\n\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    base["senha"] = input('Digite sua senha: ')
    cpf = f"'cpf': '{base['cpf']}'"
    senha = f"'senha': '{base['senha']}'"
    with open('users.txt', 'r') as file:
        data = file.readlines()
    for linha in range(len(data)):
        if cpf and senha in data[linha]:
            linhas = open('users.txt', 'r').readlines()
            linhas[linha] = f''
            change = open('users.txt', 'w')
            change.writelines(linhas)
            sleep(1)
            print('USUÁRIO EXCLUÍDO COM SUCESSO!')
            sleep(3)
            break
        elif cpf in data[linha] and senha not in data[linha]:
            sleep(0.3)
            print('\033[31mA senha informada não corresponde o CPF.\033[m')
            sleep(1)
            from main import menu
            menu()

from time import sleep
from searchuser import buscar_usuario
base = dict()


def registro():
    """
    Essa função vai perguntar o nome do cliente,o cpf do mesmo,
    tipo de conta, valor de entrada e uma senha para o usuário.
    """
    base["nome"] = str(input('Nome: '))
    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        sleep(0.3)
        print('\n\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        sleep(1)
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    base["senha"] = input('Digite a senha que será usada[5 digitos]: ')
    base["saldo"] = float(input('Digite o valor inicial que será depositar:'))
    while len(base["senha"]) != 5:
        if len(base["senha"]) != 5:
            print('\n\033[31mO formato da senha está incorreto. Ex: 12345\033[m')
            sleep(2)
        base["senha"] = input('Digite a senha que será usada[5 digitos]: ')

    buscar_usuario(base["cpf"])
    if buscar_usuario:
        with open('users.txt', 'a+', newline='') as file:
            file.writelines(f'{base}\n')
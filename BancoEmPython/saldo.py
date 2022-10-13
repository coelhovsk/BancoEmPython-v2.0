import ast
from time import sleep
base = dict()


def saldo():
    """
    """
    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        print('\n\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    base["senha"] = str(input("Digite a sua senha: "))
    cpf = f"'cpf': '{base['cpf']}'"
    senha = f"'senha': '{base['senha']}'"
    with open('users.txt', 'r') as file:
        data = file.readlines()
    for linha in range(len(data)):
        if cpf and senha in data[linha]:
            dictline = data[linha]
            converteddict = ast.literal_eval(dictline)
            sleep(1)
            print(45 * '\033[30m-=\033[m')
            print(f"Sr. {converteddict['nome']} o seu saldo atual é: {converteddict['saldo']}")
            print(45 * '\033[30m-=\033[m')
            sleep(3)
            break
        elif cpf in data[linha] and senha not in data[linha]:
            sleep(0.3)
            print('\033[31mA senha informada não corresponde o CPF.\033[m')
            sleep(1)
            from main import menu
            menu()

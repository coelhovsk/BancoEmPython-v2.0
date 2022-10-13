import ast
from time import sleep
base = dict()

def saque():
    """
    """
    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        print('\n\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    base["senha"] = input('Digite sua senha: ')
    base["debito"] = float(input("Digite o valor que deseja debitar: "))
    cpf = f"'cpf': '{base['cpf']}'"
    senha = f"'senha': '{base['senha']}'"
    with open('users.txt', 'r') as file:
        data = file.readlines()
    for linha in range(len(data)):
        if cpf and senha in data[linha]:
            dictline = data[linha]
            converteddict = ast.literal_eval(dictline)
            converteddict["saldo"] -= base["debito"]
            convertedstr = str(converteddict)
            linhas = open('users.txt', 'r').readlines()
            linhas[linha] = f'{convertedstr}\n'
            change = open('users.txt', 'w')
            change.writelines(linhas)
            break
        elif cpf in data[linha] and senha not in data[linha]:
            sleep(0.3)
            print('\033[31mA senha informada não corresponde o CPF.\033[m')
            sleep(1)
            from main import menu
            menu()

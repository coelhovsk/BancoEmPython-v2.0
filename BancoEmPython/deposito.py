import ast
base = dict()


def deposito():
    """
    """
    base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    while len(base["cpf"]) != 11:
        print('\n\033[31mO CPF informado não corresponde o formato correto. Por favor verifique-o\n'
              'Digite sem pontuação.\033[33m Ex: 12345678900\033[m')
        base["cpf"] = str(input('Informe seu CPF(sem pontuação): '))
    base["deposito"] = float(input("Digite o valor que deseja depositar: "))
    cpf = f"'cpf': '{base['cpf']}'"
    with open('users.txt', 'r') as file:
        data = file.readlines()
    for linha in range(len(data)):
        if cpf in data[linha]:
            dictline = data[linha]
            converteddict = ast.literal_eval(dictline)
            converteddict["saldo"] += base["deposito"]
            convertedstr = str(converteddict)
            linhas = open('users.txt', 'r').readlines()
            linhas[linha] = f'{convertedstr}\n'
            change = open('users.txt', 'w')
            change.writelines(linhas)
            break

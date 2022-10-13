from time import sleep

import registro
import deposito
import saque
import saldo
import apagar

base = dict()
print('-=< 𝒬𝓊𝑒𝓂 𝒫𝑜𝓊𝓅𝒶 𝒯𝑒𝓂  >=-')


def menu():
    print('1 - Novo Cliente\n'
          '2 - Depositar\n'
          '3 - Debitar\n'
          '4 - Saldo\n'
          '5 - Apagar Cliente\n')
    print()
    print('0 - Sair\n'
          ' ')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        registro.registro()
    if opcao == 2:
        deposito.deposito()
    if opcao == 3:
        saque.saque()
    if opcao == 4:
        sleep(0.3)
        saldo.saldo()
        sleep(1)
    if opcao == 5:
        sleep(0.3)
        apagar.apagar_cliente()
        sleep(1)
    if opcao == 0:
        exit()


menu()

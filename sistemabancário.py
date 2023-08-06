deposito = 0
saldo = 0
saque = 0
limite_diario = 0
limite_saque = 500
extrato = ' '
while True:
    print('~'*20)
    menu = str(
        input(' [d] Depósito \n [e] Extrato\n [s] Saque \n [q] Sair \n => ')).upper()
    print('~'*20)
    if menu == 'D':
        deposito = float(input('quanto deseja depositar? R$ '))
        if deposito < 10:
            print('-_'*30)
            print('opção inválida! depósito mínimo de R$ 10.00.')
            print('-_'*30)
        else:
            saldo += deposito
            extrato += str(f'\nDepósito:R${deposito:.2f}\n')
    elif menu == 'E':
        print('-='*10, ' EXTRATO ', '-='*10)
        print('nenhuma movimentação!'if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('-='*25)
    elif menu == 'S':
        saque = float(input('quanto deseja sacar? R$ '))
        if saque > saldo:
            print(
                'operação inválida! voçê não possui créditos em sua conta. faça um depósito!')
        elif limite_diario >= 3:
            print('você já atingiu seu limite diário! tente novamente amanhã!')
        elif saque > limite_saque:
            print('sua solicitação EXCEDE o limite de R$500.00 por saque!')
        elif saque > 0:
            saldo -= saque
            extrato += str(f'saque: R${saque:.2f}\n')
            limite_diario += 1
        else:
            print('valor inválido! digite um valor válido!')
    elif menu == 'Q':
        break
    else:
        print('ERRO! tente uma opção válida! ')

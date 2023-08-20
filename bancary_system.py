from tabulate import tabulate

menu = '''
CAIXA ELETRÔNICO BANKSYSTEM

Selecione a opção desejada:

[1] Saque
[2] Depóstio
[3] Extrato
[0] Sair

// '''
SALDO_INICIAL = 500
saldo = SALDO_INICIAL
numero_saques = 1
LIMITE_SAQUES = 3
historial_saques = []
historial_depositos = []
suma_saque = 0
suma_deposito = 0


# O caixa não aceita moedas, pelo que os únicos valores positivos que não podem ser depositados são R$1,00 e R$3,00
def possiveis_combinacoes(de, a):
    possiveis_saques = []
    for numero in range(de, a + 1):
        if numero != 3:
            possiveis_saques.append(numero)
    return possiveis_saques
possiveis_saques = possiveis_combinacoes(2, 500)
possiveis_depositos = possiveis_combinacoes(2, 2000)


while True:

    opcao = input(menu)

    if opcao == "1" and numero_saques > LIMITE_SAQUES:
        print("O máximo de saques diários foi atingido")

    elif opcao == "1" and numero_saques <= LIMITE_SAQUES:
        print("""
SAQUE
              """
              )
        saque = int(input("""
Este caixa possui notas de R$2, R$5, R$10, R$20, R$50, R$100 e R$200.
                          
O limite de saque neste caixa é de R$500,00.

Informe a quantia para o saque: R$  """)
                            )
        status = "Succes" if saque in possiveis_saques else "Error"
        if status == "Error":
            print("Valor inválido para saque.")
        elif saldo >= saque:
            print("Saque realizado com sucesso. Retire o dinheiro no local indicado.")
            saldo -= saque
            print(f"Seu novo saldo é: R${saldo},00")
            numero_saques += 1
            print(f'Saque de número {(numero_saques - 1)}')
            historial_saques.append(f'R${saque: .2f}')
            historial_depositos.append("R$0.00")
            suma_saque += saque
        else:
            print("Operação não realizada. Saldo insuficiente")

    elif opcao == "2":
        print("""
DEPÓSITO
              """
              )
        deposito = int(input("""
Este caixa não aceita moedas, apenas notas de R$2, R$5, R$10, R$20, R$50, R$100 e R$200.

O limite de depósito neste caixa é de R$2.000,00.

Informe a quantia para o depósito e insira as cédulas no local indicado: R$ """)
                       )
        status = "Success" if deposito in possiveis_depositos else "Error"
        if status == "Error":
            print("Valor inválido para depósito")
        else:
            saldo += deposito
            print(f"Seu novo saldo é: R${saldo},00")
            historial_depositos.append(f'R${deposito: .2f}')
            historial_saques.append("R$0.00")
            suma_deposito += deposito
    elif opcao == "3":
        print("""
EXTRATO BANCÁRIO
              """
              )
        extrato = list(zip(historial_depositos, historial_saques))
        cabecalho = ["Depósitos", "Saques"]
        historico = tabulate(extrato, headers=cabecalho, tablefmt="grid")
        if not extrato:
            print("Não foram realizadas movimentações")
        else:
            print(f'Saldo inicial:      R${SALDO_INICIAL}.00')
            print()
            print(historico)
            print()
            print(f'Total de depósitos: R${suma_deposito}.00')
            print(f'Total de saques:   -R${suma_saque}.00')
            print(f'Saldo da conta:     R${SALDO_INICIAL + suma_deposito - suma_saque}.00') 
    elif opcao == "0":
        print('Obrigado pela preferência. Tenha um bom dia.')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
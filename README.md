# 🏧 CAIXA ELETRÔNICO BANKSYSTEM
## Desafío Criando um Sistema Bancário com Python

O código executa a tela inicial de um sistema bancário que admite as opções de saque, depósito e consulta de extrato. Como as operações de saque e depósito comumente são realizadas em caixas eletrônicos, estabeleci alguns parâmetros:

    1. O sistema admite apenas o uso de notas, pelo que o input de um valor de saque ou depósito é um número inteiro positivo.
    2. Devido a que a nota de menor valor é R$2.00, o sistema não admite saques nem depósitos de R$1.00 e R$3.00 (seria necessário inserir uma moeda). É possível criar o restante dos números com combinações de notas.
    3. O valor máximo de saque é R$500.00 e está limitado a 3 ocorrências.
    4. O valor máximo de depósito é de R$2000.00 sem limite de ocorrências.
    5. O extrato bancário se entrega indicando o saldo inicial (R$500.00), os depósitos e os saques tabulados, a soma destas colunas e o saldo final.

Usei como modelo a arquitetura while do prof. @decarvalhogui.

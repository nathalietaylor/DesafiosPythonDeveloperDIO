#Objetivo geral: criar um sistema bancario com operações de sacar, depositar e visualizar extrato

#operação deposito:
#deve ser possível depositar valores positivos
# esta versão trabalha apenas com 1 usuário, não precisando identificar
#qual é o numero da agencia e conta bancaria.
#todos os depositos devem ser armazenados em uma variável e 
# exibidos na operação de extrato

#operação saque:
#o sistema deve permitir 3 saques diários com limite máximo de R$500,00 por saque.
#caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem
# informando que não será possível sacar o dinheiro por falta de saldo.
#Todos os saques deve ser armazenados em uma variavel e exibidos na operação de extrato

#operaçao de extrato:
#essa operação deve listar todos os depositos e saques realizados na conta.
#No fim da linguagem deve ser exibido o saldo atual da conta.
#Os valores devem ser exibidos utilizando o formato R$xxx.xx
 
menu = """
 ********** Bem Vindo! **********
 
 Escolha uma operação: 
 1- depósito
 2- saque
 3- extrato
 4- sair
 
 ********************************
 """
saldo = 0 
num_saques = 0
valor_lim_saque = 500
limite_saques = 3
extrato = ""

while True: #para um loop infinito
    opcao = input(menu)
    if opcao == "1":
        print("depósito")
        dep = float(input("Informe o valor desejado para o depósito:"))
        if dep > 0:
            saldo += dep
            extrato += f"Depósito: R${dep:.2f}\n"
            print ("Depósito realizado com sucesso")
        else:
            print("Valor inválido, digite novamente o valor desejado.\n")
            
    elif opcao == "2":
        if num_saques <= 3:
            print("saque")
            saque = float(input("Informe o valor desejado para saque:"))
            if saque > saldo:
                print("Saldo insuficiente para saque.")
                
            elif saque > valor_lim_saque:
                print("Valor limite para saque excedido.")
            
            elif saque>0:
                saldo -= saque
                extrato += f" Saque: R${saque:.2f}\n"
                print ("Saque realizado com sucesso")
                num_saques += 1
            else:
                print("Valor inválido, digite novamente o valor desejado.\n")
        else:
             print("Limite de saques atingido.")       
    elif opcao == "3":
        print("\n********** EXTRATO **********\n")
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("*****************************\n")
          
    elif opcao == "4":
        break
    else: 
        print("Opção inválida, por favor selecione novamente a opção desejada.")
        

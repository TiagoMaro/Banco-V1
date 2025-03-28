def Op_Saque(*, saldo, valor, limite_diario, limite_saque, extrato):
    saldo_insuficiente = valor > saldo
    limite_saque_atingido = valor> limite_saque
    limite_diario_atingido = limite_diario > 3

    if saldo_insuficiente:
        print("Saldo insuficiente")
    
    elif limite_diario_atingido:
        print("Seu limite diário de saque foi atingido")
    
    elif limite_saque_atingido:
        print("Seu valor de saque foi atingido")
    
    elif valor > 0:
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        saldo -= valor
    
    else:
        print("Operação falhou!")

    return saldo, extrato


def Op_Deposito(*,saldo, valor, extrato):
    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR${valor:.2f}\n"
    else:
        print("Valor não permitido")
    
    return saldo, extrato

def Op_Extrato(*,saldo, extrato):
    print(f"""
==============================
{extrato}
==============================
Saldo em conta: {saldo:.2f}
""")
    return 0



def main():
    limite_diario = 0
    LIMITE_SAQUE = 500.0
    valor_conta = 0
    extrato_conta = ""



    menu = """
    
    [d] - depositar
    [s] - sacar
    [e] - extrato
    [q] - sair

    
    ==> """


    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Qual valor deseja depositar? "))
            valor_conta, extrato_conta = Op_Deposito(saldo=valor_conta, valor=valor, extrato=extrato_conta)

        elif opcao == "s":
            limite_diario += 1
            valor = float(input("Qual valor deseja sacar? "))
            valor_conta, extrato_conta = Op_Saque(saldo=valor_conta, valor=valor, extrato=extrato_conta, limite_diario=limite_diario, limite_saque=LIMITE_SAQUE)

        elif opcao == "e":
            Op_Extrato(saldo=valor_conta, extrato=extrato_conta)
        
        elif opcao == "q":
            break

        else:
            print("Operação invalida, digite uma operação válida.")

main()
import os

def exibir_nome_do_programa():
    print("App Comido!\n")

def exibir_opcoes():
    print("1. Cadastras lancheria ")
    print("2. Listar lancheria")
    print("3. Ativar lancheria")
    print("4. Sair")

opcao_escolhida = int (input("Escolha sua escolha: \n " ))

print (f"Você escolheu a opção {opcao_escolhida}") 

def finalizar_app():
    os.system("cls")
    print("Finalizar o app")

    if opcao_escolhida == 1: 
        print ("Cadastras lancheria")
    elif opcao_escolhida == 2:
        print("Listar lancheria")
    elif opcao_escolhida == 3:
        print("Ativar lancheria")
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()

if __name__=='__main__':


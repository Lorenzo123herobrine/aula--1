print("App Comido!\n")

print("1. Cadastras lancheria ")

print("2. Listar lancheria")

print("3. Ativar lancheria")

print("4. Sair")

opcao_escolhida = int (input("Escolha sua escolha: \n " ))

print (f"Você escolheu a opção {opcao_escolhida}") 

def finalizar_app():
    print("Finalizar o app")

if opcao_escolhida == 1: 
    print ("Cadastras lancheria")

elif opcao_escolhida == 2:
    print("Listar lancheria")

elif opcao_escolhida == 3:
    print("Ativar lancheria")

else:
    finalizar_app()

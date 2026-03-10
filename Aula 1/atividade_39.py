def main():
    """Roda um menu interativo minimalista"""
    while True:
        print("\n--- MENU ---")
        print("1. Olá")
        print("2. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("Executando comando...")
        elif escolha == '2':
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")
main()
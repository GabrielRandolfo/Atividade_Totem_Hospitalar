class Menu:

    def mostrar_menu(self):
        print("[MENU DE SERVIÇOS]")
        print("1. Consulta")
        print("2. Exame")
        print("3. Emergência")

        opcao = input("Escolha a opção: ")

        if opcao == "1":
            return "Consulta"

        elif opcao == "2":
            return "Exame"

        elif opcao == "3":
            return "Emergência"

        else:
            print("Opção inválida.")
            return self.mostrar_menu()

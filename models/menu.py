class Menu:

    def mostrar_menu(self):
        print("[HOSPITAL SENAI BETIM PROJETO]")
        print("")
        print("1. Consulta")
        print("2. Exame")
        print("3. Emergência")
        print("")
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

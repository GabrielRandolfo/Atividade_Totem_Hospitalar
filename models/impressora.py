from datetime import datetime

class Impressora:

    def imprimir_ticket(self, paciente, tipo, servico, senha):

        print("\n------------------------------------------")
        print("TICKET DE ATENDIMENTO")
        print("------------------------------------------")
        print(f"PACIENTE: {paciente.nome}")

        if tipo == "Prioritário":
            print("TIPO: PRIORITÁRIO (Lei 10.048)")
        else:
            print("TIPO: Geral")

        print(f"SERVIÇO: {servico}")
        print(f"SENHA: {senha}")
        print("------------------------------------------")
        print("Aguarde ser chamado no painel central.")
        print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M"))

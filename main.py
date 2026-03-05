from models.menu import Menu
from models.paciente import Paciente
from models.classificador import Classificador
from models.triagem import Triagem
from models.gerador_senha import GeradorSenha
from models.impressora import Impressora


def main():

    menu = Menu()
    classificador = Classificador()
    triagem = Triagem()
    gerador = GeradorSenha()

    while True:

        print("\n=== TOTEM DE ATENDIMENTO ===")

        nome = input("Nome do paciente: ")
        idade = int(input("Idade: "))
        pcd_input = input("Paciente PCD? (s/n): ")

        pcd = pcd_input.lower() == "s"

        paciente = Paciente(nome, idade, pcd)

        servico = menu.mostrar_menu()

        alerta = triagem.avaliar(servico)

        if alerta:
            print("\n⚠️", alerta)
            continue

        prioridade = classificador.classificar(paciente)

        senha = gerador.gerar(prioridade)

        print("\n=== TICKET ===")
        print("Paciente:", paciente.nome)
        print("Serviço:", servico)
        print("Prioridade:", prioridade)
        print("Senha:", senha)

        print("\nRetornando ao menu...\n")


if __name__ == "__main__":
    main()
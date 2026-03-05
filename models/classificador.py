from models.paciente import Paciente

class Classificador:


    IDADE_PRIORITARIA = 60

    def classificar(self, paciente: Paciente) -> str:
        if not isinstance(paciente, Paciente):
            raise TypeError("classificar() espera um objeto do tipo Paciente.")

        if paciente.pcd or paciente.idade >= self.IDADE_PRIORITARIA:
            return "Prioritário"
        return "Normal"
from models.paciente import Paciente

class Classificador:
    """
    Decide se um Paciente é 'Prioritário' ou 'Normal'
    Regra sugerida (comum em triagem):
      - Prioritário se pcd == True
      - OU se idade >= 60
      - Caso contrário, Normal
    """

    IDADE_PRIORITARIA = 60

    def classificar(self, paciente: Paciente) -> str:
        if not isinstance(paciente, Paciente):
            raise TypeError("classificar() espera um objeto do tipo Paciente.")

        if paciente.pcd or paciente.idade >= self.IDADE_PRIORITARIA:
            return "Prioritário"
        return "Normal"